#!/bin/bash

# Define the name of the virtual environment
env_name="cvp1"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 to continue."
    exit 1
fi

# Create the virtual environment
python3 -m venv $env_name

# Activate the virtual environment
source $env_name/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Define the required dependencies
dependencies=(
    "torch"
    "torchvision"
    "matplotlib"
    "numpy"
    "scipy"
    "scikit-image"
)

# Install the dependencies
pip install "${dependencies[@]}"

# Confirm installation
echo "All dependencies have been installed in the virtual environment: $env_name"

deactivate

# Instructions to activate the environment later
echo "To activate the virtual environment in the future, run:"
echo "source $env_name/bin/activate"
