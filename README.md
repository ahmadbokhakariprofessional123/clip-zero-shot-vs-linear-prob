# Zero-Shot vs Linear Probe Comparison using CLIP (ViT-B/32)

## Clear Summary

This project investigates whether prompt engineering can improve the performance of a zero-shot CLIP model on low-resolution CIFAR-10 images, and compares it against a supervised linear probe classifier trained on frozen CLIP image embeddings.

Using 1000 fixed CIFAR-10 images, three prompting strategies were evaluated:

- Single Canonical Prompt
- Universal Prompt Ensemble
- Class-Specific Prompt Ensemble

The best zero-shot method (Class-Specific Prompt Ensemble) improved Recall@1 from 0.851 to 0.863. However, a supervised linear probe outperformed all zero-shot methods, correcting 97 out of 120 zero-shot errors.

The results show that prompt engineering helps, especially for visually ambiguous animal classes, but it cannot fully compensate for CIFAR-10’s low resolution (32×32 images).

---

## Plain Language Explanation

### What is CLIP?

CLIP (Contrastive Language–Image Pretraining) is a vision-language model trained to connect images and text.

Instead of learning from traditional labeled datasets (like “this is a dog”), CLIP was trained on hundreds of millions of image–text pairs from the internet. It learns by matching images to their correct text descriptions.

In simple terms:

- CLIP turns images into numbers (image embeddings).
- CLIP turns text into numbers (text embeddings).
- If the numbers are similar, the image and text likely match.

It does this using two transformer models:
- A Vision Transformer (for images)
- A Text Transformer (for text)

Both outputs are 512-dimensional vectors that can be compared using cosine similarity.

---

### What is Zero-Shot Learning?

Zero-shot learning means making predictions without training on the target dataset.

Instead of training on CIFAR-10 images directly, we:

1. Write text prompts like:
   - "a photo of a dog"
2. Convert them into embeddings using CLIP.
3. Compare them with image embeddings.
4. Rank images by similarity.

No model weights are updated.

The model relies entirely on its prior knowledge learned from internet data.

---

## Project Objective

To evaluate:

1. Whether prompt engineering improves zero-shot retrieval.
2. Whether class-specific prompts outperform generic prompts.
3. Whether supervised learning still performs better.
4. How low-resolution images affect performance.

---

## Dataset

CIFAR-10

- 60,000 colour images
- 32×32 resolution
- 10 classes
- 1000 fixed images used for testing (100 per class, seed = 0)
- 2000 images used for linear probe training

No fine-tuning of CLIP was allowed.

---

## Models Compared

1. Single Canonical Prompt  
   Example: "a photo of a {}"

2. Universal Prompt Ensemble  
   Six general templates averaged per class.

3. Class-Specific Prompt Ensemble  
   Six descriptive templates written specifically for each class.

4. Linear Probe  
   A supervised softmax classifier trained on frozen CLIP image embeddings.

---

## Evaluation Metrics

- Recall@1  
- Recall@5  

Recall@1 checks if the top result is correct.  
Recall@5 checks if the correct class appears in the top five results.

Recall@5 is useful because CIFAR-10 images are low resolution and often visually similar.

---

## Results (Macro Average)

| Model                   | Recall@1 | Recall@5 |
|--------------------------|----------|----------|
| Single Prompt           | 0.851    | 0.996    |
| Universal Ensemble      | 0.855    | 0.992    |
| Class-Specific Ensemble | 0.863    | 0.997    |
| Linear Probe            | Higher than all zero-shot models |

Key findings:

- Prompt ensembling improves performance.
- Class-specific prompts perform best.
- Animal classes benefit most from richer descriptions.
- Frog remains the hardest class due to low resolution.
- Linear probe significantly reduces errors.

---

## Error Analysis

- Zero-shot errors: 120  
- Linear probe errors: 26  
- Errors fixed by linear probe: 97  
- Shared errors: 23  

This shows many zero-shot errors come from text-image misalignment rather than complete visual failure.

---

## Prompt Sensitivity Index (PSI)

Macro average improvement: +0.02

This means class-specific prompt ensembling improves Recall@1 by approximately 2% compared to a single prompt.

Most sensitive class: Horse  
Least sensitive class: Automobile  

---

## Limitations

- CIFAR-10 images are extremely low resolution (32×32).
- CLIP was trained on high-resolution internet images.
- Prompt design is subjective.
- Linear probe used overlapping training and testing images (risk of overfitting).

---

## What I Learned

1. Prompt engineering matters.  
   Small wording changes can measurably affect performance.

2. Zero-shot models are powerful but fragile.  
   They rely heavily on text-image alignment.

3. Low resolution is a major bottleneck.  
   Prompt improvements cannot fully recover lost visual detail.

4. Supervised learning is still stronger when labeled data is available.  
   The linear probe significantly outperformed zero-shot retrieval.

5. Error analysis is critical.  
   Comparing which errors are fixed helps understand whether improvements come from better text alignment or better feature learning.

6. Model evaluation must consider fairness and bias.  
   CLIP’s internet pretraining introduces background and representation biases.

---

## Future Improvements

- Explore automatic prompt learning (CoOp / CoCoOp)
- Use larger CLIP models (ViT-L/14)
- Apply super-resolution preprocessing
- Evaluate on higher-resolution datasets
- Introduce safer deployment monitoring

---

## Project Structure



Jupyter Notebook

HOW TO RUN THE PROJECT
pip install -r requirements.txt
jupyter notebook Zero Shot and CLIP.ipynb
