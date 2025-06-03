import os
import re
import duckdb
import requests

METADATA = {}

def extract_sql_schema(prompt_content):
    """
    Extract SQL schema from the prompt content.
    
    Args:
        prompt_content: String containing the prompt content
        
    Returns:
        str: SQL schema statements
    """
    schema_match = re.search(r'=== SQL schema start ===(.*?)=== database schema end ===', 
                            prompt_content, re.DOTALL)
    if not schema_match:
        raise ValueError("SQL schema not found in prompt content")
    
    return schema_match.group(1).strip()

def extract_sql_query(query_text):
    """
    Extract SQL query from text that might contain markdown formatting.
    
    Args:
        query_text: String containing the SQL query possibly with markdown formatting
        
    Returns:
        str: Clean SQL query
    """
    # Try to extract from markdown SQL code block
    sql_pattern = r'```sql\s*(.*?)\s*```'
    sql_match = re.search(sql_pattern, query_text, re.DOTALL)
    
    if sql_match:
        return sql_match.group(1).strip()
    
    # If no markdown formatting, return as is
    return query_text.strip()

def is_query_runnable(conn, query):
    """
    Check if a query is runnable in DuckDB.
    
    Args:
        conn: DuckDB connection
        query: SQL query to test
        
    Returns:
        bool: True if query runs without errors
    """
    try:
        conn.execute(query)
        return True
    except Exception as e:
        print(f"Query execution error: {str(e)}")
        return False

def are_queries_functionally_equivalent(schema, query1, query2):
    """
    Use LLM as a judge to determine if two queries are functionally equivalent.
    
    Args:
        schema: SQL schema
        query1: First SQL query
        query2: Second SQL query
        
    Returns:
        bool: True if queries are judged to be functionally equivalent
    """
    model = os.environ.get('LLM_MODEL', 'google/gemini-2.5-flash-preview-05-20')
    api_key = os.environ.get('OPENROUTER_API_KEY', '')

    if not api_key:
        print("Warning: OPENROUTER_API_KEY not found in environment variables")
        return False
    
    prompt = f"""
You are an expert SQL judge. Your task is to determine if two SQL queries are functionally equivalent.
Two SQL queries are functionally equivalent if they return the same results when executed on the same database.

Database schema:
{schema}

Query 1:
{query1}

Query 2:
{query2}

Are these queries functionally equivalent? Answer with ONLY 'Yes' or 'No'.
"""
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': model,
        'messages': [
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 10
    }
    
    try:
        response = requests.post('https://openrouter.ai/api/v1/chat/completions', 
                                headers=headers, 
                                json=data)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            answer = result['choices'][0]['message']['content'].strip().lower()
            return 'yes' in answer
        
        return False
    except Exception as e:
        print(f"LLM API error: {str(e)}")
        return False

def ll_run_tests(response_data):
    """
    Main test function for text2sql_duckdb evaluation.
    Args:
        response_data: Dict containing response and truth
    Returns:
        bool: True if answers are equivalent
    """
    try:
        # Extract response and truth
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt'].get('parsed_truth', response_data['prompt'].get('truth', ''))
        
        # Clean up queries by extracting from markdown if needed
        response_query = extract_sql_query(response)
        truth_query = extract_sql_query(truth)
        
        # Get SQL schema from prompt
        prompt_messages = response_data['prompt'].get('input', [])
        schema = None
        
        for message in prompt_messages:
            if message.get('role') == 'user' and 'SQL schema' in message.get('content', ''):
                schema = extract_sql_schema(message['content'])
                break
        
        if not schema:
            print("SQL schema not found in prompt")
            return False
        
        # Initialize in-memory DuckDB database
        conn = duckdb.connect(':memory:')
        
        # Apply schema to database
        conn.execute(schema)
        
        # Test if both queries are runnable
        response_runnable = is_query_runnable(conn, response_query)
        truth_runnable = is_query_runnable(conn, truth_query)
        
        if not response_runnable:
            print("Response query is not runnable in DuckDB")
            return False
        
        if not truth_runnable:
            print("Truth query is not runnable in DuckDB - unexpected behavior")
            return False
        
        # Use LLM-as-a-judge to evaluate functional equivalence
        is_equivalent = are_queries_functionally_equivalent(schema, response_query, truth_query)
        
        return is_equivalent
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False
