import json
from typing import Any, Dict
from docetl.utils_evaluation import register_eval

@register_eval
def evaluate_results(dataset_file_path: str, results_file_path: str) -> Dict[str, Any]:
    """
    Evaluate pipeline output against the original dataset.
    """
    # Load pipeline output
    with open(results_file_path, 'r') as f:
        output = json.load(f)

    # Load original dataset for comparison
    with open(dataset_file_path, 'r') as f:
        dataset = json.load(f)

    # Compute your evaluation metrics
    correct_count = 0
    total_count = len(output)

    for idx, result in enumerate(output):
        # Compare result with original data
        # For example, if your dataset has a 'src' attribute, it's available in the output
        original_text = result.get("content", "").lower()
        extracted_items = result.get("filler_words", [])

        # Check if extracted items appear in original text
        for item in extracted_items:
            if item.lower() in original_text:
                correct_count += 1

    # Return dictionary of metrics
    return {
        "filler_extraction_score": correct_count,  # This key will be used if metric_key matches
        "total_extracted": total_count,
        "precision": correct_count / total_count if total_count > 0 else 0.0,
    }