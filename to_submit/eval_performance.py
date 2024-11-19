import os
import time
import torch
import torchvision.transforms as transforms
from torchvision.datasets import STL10
from torchvision.utils import save_image
import matplotlib.pyplot as plt


# Function to load dataset
def load_dataset(transform):
    dataset = STL10(root='./data', split='train', download=True, transform=transform)
    return torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)

# Function to evaluate performance
def evaluate_performance(transform, label):
    # Create folder for saving images
    folder_name = f'output_{label}'
    os.makedirs(folder_name, exist_ok=True)

    # Load dataset
    dataloader = load_dataset(transform)

    # Measure loading time
    start_time = time.time()
    for idx, (images, labels) in enumerate(dataloader):
        # Save the first few batches of images
        if idx < 5:  # Save only first 5 batches
            for i, img in enumerate(images):
                save_image(img, os.path.join(folder_name, f'{idx}_{i}.png'))
    end_time = time.time()

    # Return elapsed time
    return end_time - start_time

# Function to plot and save performance graph
def plot_performance(times, labels, output_file):
    plt.figure(figsize=(8, 6))
    plt.bar(labels, times, color=['blue', 'green'])
    plt.xlabel('Configuration', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=14)
    plt.title('Performance Comparison of Data Transformations', fontsize=16)
    for i, time_val in enumerate(times):
        plt.text(i, time_val + 0.1, f'{time_val:.2f}', ha='center', fontsize=12)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()