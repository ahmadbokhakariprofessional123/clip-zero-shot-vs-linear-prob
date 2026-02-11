CLIP Zero-Shot vs Linear Probe on CIFAR-10
Project Summary

This project investigates how different prompting strategies affect the performance of CLIP (ViT-B/32) in zero-shot image classification on a subset of CIFAR-10 (1000 images). Three zero-shot prompting approaches were compared (single prompt, universal ensemble, and class-specific ensemble), and the best zero-shot model was evaluated against a supervised linear probe classifier trained on CLIP embeddings.

Key Result:
Class-specific prompt ensembling achieved the best zero-shot performance (Recall@1 = 0.863), while the supervised linear probe significantly outperformed zero-shot models by correcting 97 out of 120 zero-shot errors 

.

 What is CLIP? (Plain Language Explanation)

CLIP (Contrastive Language–Image Pre-training) is a vision-language model that learns to match images with text descriptions.

Instead of training on labelled datasets like traditional classifiers, CLIP is trained on large numbers of image–caption pairs from the internet. After training, it can perform zero-shot classification, meaning:

It can classify images into new categories without being trained specifically on those categories.

CLIP works by:

Converting an image into a numerical embedding

Converting a text prompt (e.g., “a photo of a dog”) into another embedding

Comparing similarity between the two embeddings

The most similar text description becomes the predicted class.

Problem Statement

We evaluated how different prompt designs influence zero-shot classification performance on CIFAR-10 (32×32 resolution images). We compared four modelling conditions:

Single canonical prompt

Universal prompt ensemble

Class-specific prompt ensemble

Supervised linear probe classifier

The goal was to understand:

How sensitive CLIP is to prompt wording

Whether prompt engineering improves performance

How zero-shot compares to supervised adaptation

📊 Dataset

Dataset: CIFAR-10

Images used: 1000 (100 per class, fixed seed = 0)

Image size: 32×32

Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

All zero-shot models used a frozen CLIP encoder.
The linear probe was trained on CLIP image embeddings only.

🧪 Methodology
Zero-Shot Prompting Strategies

Single Canonical Prompt
Example: “a photo of a {class}”

Universal Prompt Ensemble
Multiple general templates averaged together to reduce prompt sensitivity.

Class-Specific Prompt Ensemble
Manually designed descriptive prompts tailored to each class.
Example (airplane):

“a flying airplane”

“a jet aircraft in the sky”

Embeddings were L2-normalised and averaged to create class prototypes.

Linear Probe Model

CLIP image encoder kept frozen

512-dimensional embeddings extracted

Softmax regression classifier trained on embeddings

Evaluated using Recall@1 and Recall@5
