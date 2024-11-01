import os
import json
import requests
from typing import Dict, Any, Optional
import time

METADATA = {}

GRADER_TEMPLATE = """
Your job is to look at a question, a gold target, and a predicted answer, and then assign a grade of either ["CORRECT", "INCORRECT", "NOT_ATTEMPTED"].
First, I will give examples of each grade, and then you will grade a new example.

The following are examples of CORRECT predicted answers.
```
Question: What are the names of Barack Obama's children?
Gold target: Malia Obama and Sasha Obama
Predicted answer 1: sasha and malia obama
Predicted answer 2: most people would say Malia and Sasha, but I'm not sure and would have to double check
Predicted answer 3: Barack Obama has two daughters: Malia and Sasha.
```
These predicted answers are all CORRECT because:
    - They fully contain the important information in the gold target
    - They do not contain information that contradicts the gold target
    - Capitalization, punctuation, grammar, and order don't matter
    - Hedging is okay if the correct answer is included without contradictions

The following are examples of INCORRECT predicted answers.
```
Question: What are the names of Barack Obama's children?
Gold target: Malia and Sasha
Predicted answer 1: Malia.
Predicted answer 2: Malia, Sasha, and Susan.
Predicted answer 3: Barack Obama does not have any children.
```
These predicted answers are all INCORRECT because:
    - They contain factual contradictions with the gold target
    - Even hedged incorrect statements are considered incorrect

The following are examples of NOT_ATTEMPTED predicted answers.
```
Question: What are the names of Barack Obama's children?
Gold target: Malia and Sasha
Predicted answer 1: I don't know.
Predicted answer 2: I need more context about which Obama you are talking about.
Predicted answer 3: Barack Obama has two children, but I don't recall their names.
```
These predicted answers are all NOT_ATTEMPTED because:
    - They don't include the required information
    - They don't contradict the gold target

Important notes:
- Numbers must match to the last significant figure in the gold target
- Only information directly asked in the question is required
- Information clearly inferred from the question can be omitted
- Name typos are acceptable if the identity is clear

Grade the following as either A (CORRECT), B (INCORRECT), or C (NOT_ATTEMPTED):
```
Question: {question}
Gold target: {target}
Predicted answer: {predicted_answer}
```
Just return A, B, or C with no additional text.
"""

def call_grader_model(prompt: str) -> str:
    """Call grader model via OpenRouter with retry mechanism."""
    api_key = os.getenv('OpenRouterApiKey')
    if not api_key:
        print("ERROR: OpenRouterApiKey not found in environment")
        return 'C'
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "openai/chatgpt-4o-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    max_retries = 3  # Maximum number of retries
    delay_seconds = 5  # Delay between retries in seconds

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=300
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()
                if content in ['A', 'B', 'C']:
                    print(f"Grading Result: {content}")  # This will go to stdout via capture
                    return content
                print(f"Invalid grade received: {content}")
            else:
                print(f"Response status code: {response.status_code}, response text: {response.text}")
        except Exception as e:
            print(f"Error calling grader (attempt {attempt}): {str(e)}")
        
        if attempt < max_retries:
            print(f"Retrying in {delay_seconds} seconds...")
            time.sleep(delay_seconds)
    # After retries exhausted
    print("Max retries reached. Returning 'C' as default.")
    return 'C'  # Default to NOT_ATTEMPTED on any issues

def ll_run_tests(response_data: Dict[str, Any]) -> bool:
    """
    Main test function for SimpleQA evaluation.
    Returns just a boolean as expected by scoring_runner.py.
    All output should use print() as it will be captured by OutputCapture.
    """
    try:
        # Extract data
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt'].get('parsed_truth', response_data['prompt'].get('truth', ''))
        question = response_data['prompt']['input'][0]['content']

        print(f"\nProcessing Question: {question}")
        print(f"Truth: {truth}")
        print(f"Response: {response}\n")

        # Format grading prompt
        prompt = GRADER_TEMPLATE.format(
            question=question,
            target=truth,
            predicted_answer=response
        )
        
        # Get grade and return True only if grade is 'A'
        grade = call_grader_model(prompt)
        return grade == 'A'
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False