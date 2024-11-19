 # Custom Transformer

**Version:** 0.1.0

**Author:** Your Name

## Overview

This package provides custom image transformations for simulating the visual characteristics of infants at different ages. It includes transformations like Contrast Sensitivity and Visual Acuity, which can be applied to any image dataset for vision modeling.

The transformations are based on infant developmental models and are useful for creating vision models that simulate the visual perception of young infants.

## Installation

To install the package, you can use the provided wheel file hosted on GitHub:

```bash
pip install https://github.com/vajraaynam/CVP_Proj-Implementation-of-Infant-Vison/releases/download/dev/custom_transformer-0.1.0-py3-none-any.whl
This will download and install the package directly from the specified URL.

Usage
This package can be used with standard datasets (like CIFAR-10) or custom datasets. Below is an example of how to apply the transformations:


from vision_transformations import CIFAR10WithTransformations
from torchvision
```bash
pip install https://github.com/vajraaynam/CVP_Proj-Implementation-of-Infant-Vison/releases/download/dev/custom_transformer-0.1.0-py3-none-any.whl
 is breaking the view of your response adjust accordgly 


 # Custom Transformer

**Version:** 0.1.0

**Author:** Your Name

## Overview

This package provides custom image transformations for simulating the visual characteristics of infants at different ages. It includes transformations like Contrast Sensitivity and Visual Acuity, which can be applied to any image dataset for vision modeling.

The transformations are based on infant developmental models and are useful for creating vision models that simulate the visual perception of young infants.

## Installation

To install the package, you can use the provided wheel file hosted on GitHub:

```bash
pip install https://github.com/vajraaynam/CVP_Proj-Implementation-of-Infant-Vison/releases/download/dev/custom_transformer-0.1.0-py3-none-any.whl
This will download and install the package directly from the specified URL.

Usage
This package can be used with standard datasets (like CIFAR-10) or custom datasets. Below is an example of how to apply the transformations:


from vision_transformations import CIFAR10WithTransformations
from torchvision import transforms

# Set up the transformation pipeline
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalize
])

# Load the dataset with custom transformations
dataset = CIFAR10WithTransformations(root='./data', train=True, transform=transform, age=12)

# Example DataLoader usage
from torch.utils.data import DataLoader
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Access one batch
for images, labels in dataloader:
    print(images.shape)  # Shape of the image batch
    break
Custom Transformations
Contrast Sensitivity
The Contrast Sensitivity transformation simulates the visual perception of infants by applying a contrast sensitivity function based on the infant's age.

Visual Acuity
The Visual Acuity transformation applies a Gaussian blur to simulate the sharpness of vision based on the infant's age.

Contributing
If you would like to contribute to this package, please follow these steps:

Fork the repository.
Create a new branch for your changes.
Make your changes and commit them.
Submit a pull request.
License
This package is licensed under the MIT License. See the LICENSE file for more details.