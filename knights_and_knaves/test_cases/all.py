from typing import Dict, Any

class KKProcessor:
   """Knights and Knaves response processor"""
   
   def __init__(self, cot=True, no_linebreak=True):
       self.cot = cot
       self.no_linebreak = no_linebreak

   def _parse_cot_eval(self, pred_str: str, ans: str, model_name=None):
       """Parse and evaluate response"""
       conclusion_patterns = ['CONCLUSION:', 'Conclusion:', 'conclusion:']
       
       def judge_string(input_str, reformat_gold_conditions):
           for gold_condition in reformat_gold_conditions:
               if gold_condition not in input_str:
                   return False
           return True

       # Clean and parse truth conditions
       gold = ans.replace(" and ", "").replace(".", "")
       gold_conditions = gold.split("\n")
       reformat_gold_conditions = [condition.strip() for condition in gold_conditions]

       # Find conclusion section
       pred_str = pred_str.split("### Question")[0]
       pred_answer = pred_str

       # Look for conclusion marker
       for pattern in conclusion_patterns:
           pred = pred_str.split(pattern)
           if len(pred) > 1 and len(pred[1]) > 0:
               pred_answer = pred[1]
               return judge_string(pred_answer, reformat_gold_conditions), pred_answer, reformat_gold_conditions

       return False, pred_answer, reformat_gold_conditions

def ll_run_tests(response_data: Dict[str, Any]) -> bool:
   """
   Main test function for Knights and Knaves scoring
   Args:
       response_data: Dict containing:
           - parsed_result or result: Model's response
           - prompt: Dict with truth field containing correct answer
   Returns:
       bool: True if response matches truth exactly
   """
   try:
       # Initialize processor
       processor = KKProcessor()
       
       # Get response and truth
       response = response_data.get('parsed_result', response_data.get('result', ''))
       truth = response_data['prompt']['truth']
       
       # Return True only if exact match found
       is_correct, _, _ = processor._parse_cot_eval(response, truth)
       return is_correct

   except Exception as e:
       print(f"Test failed: {str(e)}")
       return False

# Optional metadata dict
METADATA = {}