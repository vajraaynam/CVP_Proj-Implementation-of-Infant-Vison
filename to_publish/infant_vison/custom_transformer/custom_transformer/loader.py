def load_dataset(dataset_class, transform=None, age=16, **dataset_kwargs):
    """
    Load any dataset with the given transform and additional arguments, with customizable age.

    Args:
        dataset_class (torchvision.datasets.Dataset): The dataset class to be loaded (e.g., STL10, CIFAR10).
        transform (callable, optional): A transform to be applied to the dataset.
        age (int): The age parameter to be passed to the contrast sensitivity and visual acuity transformations.
        **dataset_kwargs: Additional keyword arguments for the dataset class (e.g., 'split', 'download').

    Returns:
        torch.utils.data.DataLoader: DataLoader for the specified dataset.
    """
    # Adjust the transform to use the age parameter
    if transform is not None:
        # Modify the transforms to pass the age parameter to both ContrastSensitivity and VisualAcuity
        custom_transform = transforms.Compose([
            transforms.ToTensor(),
            ContrastSensitivity(age=age),  # Pass age dynamically
            VisualAcuity(age=age),  # Pass age dynamically
            *transform.transforms  # Add any other transformations if specified
        ])
    else:
        # Default transform if none is provided
        custom_transform = transforms.Compose([
            transforms.ToTensor(),
            ContrastSensitivity(age=age),
            VisualAcuity(age=age)
        ])

    # Load the dataset with the specified transform
    dataset = dataset_class(root='./data', transform=custom_transform, **dataset_kwargs)
    return torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)