#!/usr/bin/env python3
import json
from typing import Dict, Any
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
import nltk

# Download required NLTK data
nltk.download('punkt', quiet=True)

METADATA = {}

# add rouge 1,2,L

def ll_run_tests(response_data: Dict[str, Any]) -> float:
    """
    Main test function for BLEU score evaluation.
    Returns the BLEU score as a float between 0 and 1.
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
        
        # Create result object matching ExecutionResult structure
        result = {
            "score": float(bleu_score),  # Ensure score is float
            "details": {
                "reference_tokens": len(reference[0]),
                "candidate_tokens": len(candidate)
            }
        }
        
        print(json.dumps(result))
        return float(bleu_score)  # Return float score
        
    except Exception as e:
        result = {
            "score": 0.0,  # Return 0.0 as float on error
            "details": {
                "error": str(e)
            }
        }
        print(json.dumps(result))
        return 0.0  # Return float