#!/usr/bin/env python3
import json
from typing import Dict, Any
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
import nltk
from rouge_score import rouge_scorer

# Download required NLTK data
nltk.download('punkt', quiet=True)

METADATA = {}

def ll_run_tests(response_data: Dict[str, Any]) -> float:
    """
    Main test function for BLEU and ROUGE score evaluation.
    Returns the BLEU score as a float between 0 and 1, and provides ROUGE scores in the details.
    """
    try:
        # Extract data
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt'].get('parsed_truth', response_data['prompt'].get('truth', ''))
        
        # Calculate BLEU score
        reference = [word_tokenize(truth.lower())]
        candidate = word_tokenize(response.lower())
        bleu_score = sentence_bleu(reference, candidate)
        
        # Calculate ROUGE scores
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        rouge_scores = scorer.score(truth, response)
        
        # Create result object
        result = {
            "score": float(bleu_score),
            "details": {
                "rouge1_f": float(rouge_scores['rouge1'].fmeasure),
                "rouge2_f": float(rouge_scores['rouge2'].fmeasure),
                "rougeL_f": float(rouge_scores['rougeL'].fmeasure),
                "reference_tokens": len(reference[0]),
                "candidate_tokens": len(candidate)
            }
        }
        
        print(json.dumps(result))
        return float(bleu_score)
        
    except Exception as e:
        result = {
            "score": 0.0,
            "details": {
                "error": str(e)
            }
        }
        print(json.dumps(result))
        return 0.0