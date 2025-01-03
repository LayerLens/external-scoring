#!/usr/bin/env python3
import json
from typing import Dict, Any
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
import nltk

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
except:
    pass

METADATA = {}

def ll_run_tests(response_data: Dict[str, Any]) -> bool:
    """
    Main test function for BLEU score evaluation.
    Returns a boolean indicating if the translation meets quality threshold.
    """
    try:
        # Extract data
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt'].get('parsed_truth', response_data['prompt'].get('truth', ''))
        
        # Tokenize the reference and candidate translations
        reference = [word_tokenize(truth.lower())]
        candidate = word_tokenize(response.lower())
        
        # Calculate BLEU score
        bleu_score = sentence_bleu(reference, candidate)
        
        # Print details for debugging
        print(f"\nReference: {truth}")
        print(f"Candidate: {response}")
        print(f"BLEU Score: {bleu_score:.4f}")
        
        # Consider translation successful if BLEU score is above threshold
        threshold = 0.5
        success = bleu_score >= threshold
        
        # Create result object matching ExecutionResult structure
        result = {
            "success": success,
            "details": {
                "bleu_score": bleu_score,
                "threshold": threshold,
                "reference_tokens": len(reference[0]),
                "candidate_tokens": len(candidate)
            }
        }
        
        print(f"Success: {success} (threshold: {threshold})")
        print(json.dumps(result))  # Print as JSON for scoring_runner.py to parse
        return result["success"]  # Return just the boolean for backward compatibility
        
    except Exception as e:
        error_result = {
            "success": False,
            "details": {},
            "error": str(e)
        }
        print(json.dumps(error_result))
        return False

if __name__ == "__main__":
    # Example usage
    test_data = {
        "result": "This is a test translation.",
        "prompt": {
            "truth": "This is the reference translation."
        }
    }
    success = ll_run_tests(test_data)
    print(f"Test {'passed' if success else 'failed'}")
