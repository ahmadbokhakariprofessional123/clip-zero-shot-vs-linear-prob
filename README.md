CLIP Zero-Shot vs Linear Probe on CIFAR-10
PROJECT OVERVIEW

This project evaluates the performance of OpenAI’s CLIP (ViT-B/32) model in zero-shot image classification on a subset of CIFAR-10 and compares it with a supervised linear probe classifier trained on frozen CLIP image embeddings.

The objective was to analyse how different prompting strategies affect zero-shot performance and to understand when supervised adaptation improves classification results.

DATASET

Dataset: CIFAR-10
Subset Size: 1000 images (100 per class)
Image Resolution: 32 by 32
Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
Random Seed: Fixed to ensure reproducibility

All zero-shot experiments used a frozen CLIP encoder.
The linear probe was trained using extracted CLIP image embeddings.

METHODOLOGY
Zero-Shot Prompting Strategies

Three prompting approaches were evaluated:

Single Canonical Prompt
Example: "a photo of a class"

Universal Prompt Ensemble
Multiple general templates were averaged together to reduce prompt sensitivity.

Class-Specific Prompt Ensemble
Descriptive prompts were manually designed for each class, such as
"a flying airplane" or "a jet aircraft in the sky".

Text embeddings were normalised and averaged to form class prototypes.

Linear Probe Model

CLIP image encoder kept frozen

512-dimensional embeddings extracted

Softmax regression classifier trained on embeddings

Evaluated using Recall at 1 and Recall at 5

RESULTS
Zero-Shot Performance (Macro Average)
Method	Recall at 1	Recall at 5
Single Prompt	0.851	0.996
Universal Ensemble	0.855	0.992
Class-Specific Ensemble	0.863	0.997
Linear Probe vs Zero-Shot Error Comparison

Zero-Shot Errors: 120
Linear Probe Errors: 26
Errors Fixed by Linear Probe: 97
Errors Introduced by Linear Probe: 3
Shared Errors: 23

KEY RESULTS

Class-specific prompt ensembling achieved the best zero-shot performance with Recall at 1 equal to 0.863

Prompt engineering improved performance by approximately 1 to 2 percent

The supervised linear probe significantly outperformed zero-shot methods

Most zero-shot errors were corrected by supervised adaptation

Low-resolution images limited overall model performance

LIMITATIONS AND FUTURE IMPROVEMENTS

Current limitations

CIFAR-10 resolution is much lower than CLIP’s original training data

Prompt design is subjective

Linear probe trained and tested on overlapping data which may cause overfitting

Domain mismatch between CLIP pre-training data and CIFAR images

Potential improvements

Evaluate performance on higher-resolution datasets

Perform strict train and test separation for linear probe

Test larger CLIP model variants

Explore automated prompt optimisation

WHAT IS CLIP AND ZERO-SHOT CLASSIFICATION

CLIP, which stands for Contrastive Language–Image Pre-training, is a vision-language model trained on image and text pairs collected from the internet.

Instead of learning from labelled categories directly, CLIP learns to align images and text descriptions in a shared embedding space.

Zero-shot classification means the model can classify images into new categories without being explicitly trained on those categories.

The process works by converting images and text prompts into numerical embeddings and selecting the class whose text embedding is most similar to the image embedding.

WHAT I LEARNED

How zero-shot classification works using vision-language models

How prompt wording directly affects model performance

Why prompt ensembling stabilises predictions

How frozen embeddings can be reused for supervised downstream tasks

The difference between retrieval-style classification and supervised training

How structured error analysis reveals model behaviour

TOOLS AND TECHNOLOGIES

Python

PyTorch

Hugging Face Transformers

OpenAI CLIP ViT-B/32

NumPy

Matplotlib

Jupyter Notebook

HOW TO RUN THE PROJECT
pip install -r requirements.txt
jupyter notebook Zero Shot and CLIP.ipynb
