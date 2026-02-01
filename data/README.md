# Data (CIFAR-10)

This project uses the **CIFAR-10** dataset.

✅ **Note:** The dataset is **not included** in this repository to keep the repo lightweight and to respect dataset distribution/licensing conventions.

---

## Option A: Automatically download using torchvision (recommended)

The notebook will download CIFAR-10 automatically if you use torchvision with `download=True`.

Example (the notebook already does something similar):

```python
from torchvision.datasets import CIFAR10

dataset = CIFAR10(root="./data", train=False, download=True)
