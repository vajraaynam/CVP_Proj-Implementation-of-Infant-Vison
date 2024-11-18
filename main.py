# main.py
from workers import ContrastSensitivity, VisualAcuity, display_images
from torchvision import transforms


def main():
    custom_transform = transforms.Compose([
    transforms.ToTensor(),
    ContrastSensitivity(age=16),  # Adjust age as required
    VisualAcuity(age=16)])  

    no_transform = [transforms.ToTensor()]


    display_images(transform=custom_transform, no_transform=no_transform)
if __name__ == "__main__":
    main()
