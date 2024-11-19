from torchvision import transforms
from torchvision.datasets import STL10
import torch
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2, fftshift, ifft2
from skimage.color import rgb2gray
from torchvision.transforms.functional import gaussian_blur


class ContrastSensitivity:
    def __init__(self, age):
        """
        Initialize the transformation with the age of the infant (in weeks).
        """
        self.age = age

    @staticmethod
    def contrast_sensitivity(v, c, a):
        """
        Contrast sensitivity function: s(v) = c * exp(-a * v)
        """
        return c * np.exp(-a * v)

    def csf_filter(self, shape, c, a):
        """
        Create a 2D contrast sensitivity filter in the frequency domain.
        """
        rows, cols = shape
        center_row, center_col = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        distances = np.sqrt((y - center_row) ** 2 + (x - center_col) ** 2)
        return self.contrast_sensitivity(distances, c, a)

    def peak_sensitivity(self):
        """
        Logistic growth model for peak sensitivity (c) as a function of age (weeks).
        """
        return 450 / (1 + np.exp(-0.3 * (self.age - 10)))  # Adjust parameters as needed

    def roll_off_rate(self):
        """
        Linear decline in roll-off rate (a) with age.
        """
        return max(0.4 - 0.01 * self.age, 0.1)  # Prevent a from becoming negative

    def __call__(self, image):
        """
        Transform an image based on infant contrast sensitivity at a given age.
        """
        # Define parameters based on age
        c = self.peak_sensitivity()  # Peak sensitivity
        a = self.roll_off_rate()     # Roll-off rate

        # Convert image to grayscale
        if image.shape[0] == 3:  # Check if the image has 3 channels (RGB)
            image = rgb2gray(image.numpy().transpose(1, 2, 0))  # Convert to grayscale

        # Fourier Transform
        freq_image = fftshift(fft2(image))

        # Apply CSF filter
        csf = self.csf_filter(freq_image.shape, c, a)
        filtered_image = freq_image * csf

        # Inverse Fourier Transform
        reconstructed_image = np.abs(ifft2(fftshift(filtered_image)))

        return torch.tensor(reconstructed_image, dtype=torch.float32).unsqueeze(0)  # Add channel dimension


class VisualAcuity:
    def __init__(self, age):
        """
        Initialize the visual acuity transformation with the age in months.
        """
        self.age = age

    def compute_acuity_scale(self):
        """
        Map age in months to the 20/20 to 20/600 visual acuity scale.
        """
        max_age = 24  # Age in months at which full acuity (20/20) is reached
        max_acuity = 20  # 20/20 vision
        min_acuity = 600  # 20/600 vision (newborns)
        return max(min_acuity - (self.age / max_age) * (min_acuity - max_acuity), max_acuity)

    def compute_sigma(self):
        """
        Compute the Gaussian blur sigma based on visual acuity scale.
        """
        acuity_scale = self.compute_acuity_scale()
        # Map the visual acuity scale to a Gaussian sigma (inversely proportional)
        max_sigma = 4.0  # Maximum blur
        min_sigma = 0.5  # Minimum blur
        return max_sigma * (acuity_scale / 600)  # Normalize using the max acuity value (20/600)

    def gaussian_blur(self, image, sigma):
        """
        Apply Gaussian blur to an image tensor.
        """
        kernel_size = int(2 * round(3 * sigma) + 1)
        kernel_size = max(kernel_size, 3)  # Ensure kernel size is at least 3
        return gaussian_blur(image, [kernel_size, kernel_size])

    def __call__(self, image):
        """
        Apply the visual acuity transformation to the input image.
        """
        # Handle grayscale image (H, W) by adding a channel dimension
        if image.ndim == 2:  # Grayscale input
            image = image.unsqueeze(0)

        # Compute the blur sigma based on visual acuity
        sigma = self.compute_sigma()

        # Apply Gaussian blur
        blurred_image = self.gaussian_blur(image, sigma)

        return torch.tensor(blurred_image, dtype=torch.float32)

def load_dataset(transform):
    """
    Load the STL10 dataset with the given transform.
    """
    dataset = STL10(root='./data', split='train', download=True, transform=transform)
    return torch.utils.data.DataLoader(dataset, batch_size=5, shuffle=False)


def display_images(transform, no_transform):
    """
    Display a batch of images with no transform (top) and with transform (bottom).
    """
    # Load the datasets
    no_transform_loader = load_dataset(transform=transforms.Compose(no_transform))
    transform_loader = load_dataset(transform=transform)

    # Get the first batch from each DataLoader
    no_transform_images, no_transform_labels = next(iter(no_transform_loader))
    transform_images, transform_labels = next(iter(transform_loader))

    # Convert from (batch_size, C, H, W) to (batch_size, H, W, C) for plotting
    no_transform_images = no_transform_images.numpy().transpose((0, 2, 3, 1))
    transform_images = transform_images.numpy().transpose((0, 2, 3, 1))

    # Plot the images
    fig, axes = plt.subplots(2, 5, figsize=(12, 8))  # Two rows: top (no transform), bottom (with transform)

    for i in range(5):
        # Top row: No transform
        axes[0, i].imshow(no_transform_images[i], cmap='gray')
        axes[0, i].set_title(f"No Transform\nClass: {no_transform_labels[i].item()}")
        axes[0, i].axis('off')

        # Bottom row: With transform
        axes[1, i].imshow(transform_images[i], cmap='gray')
        axes[1, i].set_title(f"Transform\nClass: {transform_labels[i].item()}")
        axes[1, i].axis('off')

    plt.tight_layout()
    plt.savefig('ausgabe_bild.png')
    plt.show()
    