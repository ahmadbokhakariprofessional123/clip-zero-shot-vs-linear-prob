# Zero-Shot Image Classification with CLIP  
### Prompt Engineering vs Linear Probe (CIFAR-10)

This project evaluates **zero-shot CLIP** for image classification and compares different **prompt engineering strategies** against a **linear probe** trained on **frozen CLIP embeddings**.

The core idea: *How much can we improve CLIP zero-shot performance by changing prompts—without training—compared to a lightweight supervised baseline?*

---

## What’s inside

### Methods
- **Zero-shot CLIP (single prompt)**  
  Uses one canonical template per class (e.g., `"a photo of a {class}"`).

- **Universal prompt ensemble**  
  Uses multiple generic templates shared across all classes; averages text embeddings per class.

- **Class-specific prompt ensemble**  
  Uses custom prompt sets per class to better match visual semantics; averages text embeddings per class.

- **Linear probe (supervised baseline)**  
  Trains a linear classifier on **frozen CLIP image embeddings**.

### Evaluation
- Dataset: **CIFAR-10**
- Metrics: **Recall@1** and **Recall@5** (retrieval-style classification via cosine similarity)

More details + results are in the included report.

---

## Repository structure

