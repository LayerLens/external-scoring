#!/usr/bin/env python3
import json
from typing import Dict, Any
import sacrebleu
from sacrebleu.metrics import BLEU

METADATA = {}

def ll_run_tests(response_data: Dict[str, Any]) -> float:
    """
    Main test function for BLEU score evaluation using sacrebleu.
    Returns the BLEU score as a float between 0 and 100.
    """
    try:
        # Extract data
        response = response_data.get('parsed_result', response_data.get('result', ''))
        truth = response_data['prompt'].get('parsed_truth', response_data['prompt'].get('truth', ''))
        
        # Calculate BLEU score using sacrebleu
        # sacrebleu expects a list of references and a list of hypotheses
        references = [truth]
        hypothesis = [response]
        
        # Create a BLEU scorer with standard WMT settings
        bleu = BLEU(
            smooth_method='exp',  # exponential smoothing
            tokenize='13a',       # standard WMT tokenization
            lowercase=True        # case insensitive comparison
        )
        
        # Calculate the BLEU score
        bleu_score = bleu.corpus_score(hypothesis, [references])
        
        # Create result object
        result = {
            "score": bleu_score.score,
            "details": {
                "bleu": bleu_score.score,
                "precisions": bleu_score.precisions,
                "brevity_penalty": bleu_score.bp,
                "length_ratio": bleu_score.sys_len / bleu_score.ref_len,
                "reference_length": bleu_score.ref_len,
                "system_length": bleu_score.sys_len
            }
        }
        
        print(json.dumps(result))
        return bleu_score.score
        
    except Exception as e:
        result = {
            "score": 0.0,
            "details": {
                "error": str(e)
            }
        }
        print(json.dumps(result))
        return 0.0