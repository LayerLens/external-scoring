
import json
import importlib
import sys
import os
from typing import Dict, Any, List

def run_tests_for_task(task_id: str, response: str) -> bool:
    try:
        # Modify task_id to create valid Python module name
        module_name = task_id.replace('/', '_').replace('.', '_')
        
        # Import test module dynamically
        test_module = importlib.import_module(f'tests.{module_name}')
        
        # Execute response code
        exec(response, globals())
        
        # Run tests
        test_module.run_tests()
        return True
        
    except Exception as e:
        print(f"Error in task {task_id}: {str(e)}")
        return False

def main(input_file: str) -> None:
    results = []
    
    with open(input_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            task_id = data['id']
            
            # Extract code from response
            try:
                response_data = json.loads(data.get('response', '{}'))
                response = response_data.get('code', '')
            except json.JSONDecodeError:
                response = data.get('response', '')
            
            success = run_tests_for_task(task_id, response)
            results.append({
                'task_id': task_id,
                'success': success
            })
    
    # Calculate pass rate
    pass_rate = sum(1 for r in results if r['success']) / len(results)
    print(f"Overall pass rate: {pass_rate:.2%}")
    
    # Output detailed results
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_jsonl_file>")
        sys.exit(1)
    main(sys.argv[1])
