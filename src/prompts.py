"""
Prompt templates for zero-shot CLIP classification on CIFAR-10.

Keep all prompts in one place so experiments are easy to reproduce and modify.
"""

from typing import Dict, List

CIFAR10_CLASSES: List[str] = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]

# Single canonical prompt
SINGLE_TEMPLATE: List[str] = ["a photo of a {c}"]

# Universal prompt ensemble (shared across classes)
UNIVERSAL_ENSEMBLE: List[str] = [
    "a photo of a {c}",
    "a close-up photo of a {c}",
    "a blurry photo of a {c}",
    "a bright photo of a {c}",
    "a photo of the {c}",
    "a good photo of a {c}",
]

# Class-specific prompt ensembles (custom per class)
# Edit these to match your notebook exactly if you used different ones.
CLASS_SPECIFIC: Dict[str, List[str]] = {
    "airplane": ["a photo of an airplane", "a photo of a jet", "a photo of an aircraft"],
    "automobile": ["a photo of a car", "a photo of an automobile", "a photo of a vehicle"],
    "bird": ["a photo of a bird", "a photo of a small bird", "a photo of a flying bird"],
    "cat": ["a photo of a cat", "a photo of a kitten", "a close-up photo of a cat"],
    "deer": ["a photo of a deer", "a photo of a wild deer", "a photo of a deer in nature"],
    "dog": ["a photo of a dog", "a photo of a puppy", "a close-up photo of a dog"],
    "frog": ["a photo of a frog", "a photo of a green frog", "a close-up photo of a frog"],
    "horse": ["a photo of a horse", "a photo of a running horse", "a photo of a horse outdoors"],
    "ship": ["a photo of a ship", "a photo of a boat", "a photo of a ship on water"],
    "truck": ["a photo of a truck", "a photo of a lorry", "a photo of a cargo truck"],
}


def get_templates(mode: str) -> Dict[str, List[str]]:
    """
    Returns dict mapping class -> list of prompt templates.
    mode: one of {"single", "universal", "class_specific"}.
    """
    mode = mode.lower().strip()
    if mode == "single":
        return {c: SINGLE_TEMPLATE for c in CIFAR10_CLASSES}
    if mode == "universal":
        return {c: UNIVERSAL_ENSEMBLE for c in CIFAR10_CLASSES}
    if mode == "class_specific":
        return CLASS_SPECIFIC
    raise ValueError(f"Unknown prompt mode: {mode}")
