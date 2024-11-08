# all.py
import re

def clean_text(text):
    """Clean and standardize text format"""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Standardize 'is a' phrases
    text = text.replace('  ', ' ')
    return text.strip()

def parse_statements(text):
    """Parse statements into normalized format"""
    try:
        statements = set()
        # Get text after the last CONCLUSION: if it exists
        if "CONCLUSION:" in text.upper():
            text = text.upper().split("CONCLUSION:")[-1]
        
        # Find all numbered statements
        lines = text.strip().split('\n')
        for line in lines:
            line = clean_text(line)
            # Look for (number) pattern
            match = re.search(r'\(\d+\)\s*(.*)', line)
            if match:
                content = match.group(1).strip()
                # Extract name and status
                if ' is a ' in content.lower():
                    parts = content.lower().split(' is a ')
                    name = parts[0].strip().title()  # Normalize name capitalization
                    status = parts[1].strip().lower()
                    if status in ['knight', 'knave']:
                        statements.add((name, status))
        
        return statements
    except Exception as e:
        print(f"Parse error: {str(e)}")
        return set()

def ll_run_tests(response_data):
    """Order-independent scoring function"""
    try:
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt']['truth']
        
        if not response or not truth:
            return False
            
        # Parse both into sets of (name, status) tuples
        truth_statements = parse_statements(truth)
        response_statements = parse_statements(response)
        
        # Both must have the same number of statements
        if len(truth_statements) != len(response_statements):
            return False
            
        # Compare sets (order independent)
        return truth_statements == response_statements
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False

# Optional metadata dict
METADATA = {}