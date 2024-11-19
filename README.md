# Python Virtual Environment Setup Script

This script automates the process of setting up a Python virtual environment and installing the required dependencies. It ensures that you have a clean and isolated environment for your Python projects.

## Prerequisites

- Ensure that Python3 is installed on your system.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. **Make the Script Executable**:
    ```bash
    chmod +x setup_env.sh
    ```
3. **Run the Script**:
    ```bash
    ./setup_env.sh
    ```

## Script Details

### Steps Performed by the Script

1. **Check for Python3 Installation**:
    - The script checks if Python3 is installed on your system. If not, it prompts you to install Python3.
2. **Create the Virtual Environment**:
    - The script creates a virtual environment named `my_env`.
3. **Activate the Virtual Environment**:
    - The script activates the virtual environment.
4. **Upgrade Pip**:
    - The script upgrades `pip` to the latest version.
5. **Install Dependencies**:
    - The script installs the following dependencies:
        - `torch`
        - `torchvision`
        - `matplotlib`
        - `numpy`
        - `scipy`
        - `scikit-image`
6. **Deactivate the Virtual Environment**:
    - The script deactivates the virtual environment after installing the dependencies.
7. **Instructions for Future Activation**:
    - The script provides instructions on how to activate the virtual environment in the future.

### Error Handling

- The script includes error handling to ensure that each step is successfully completed. If any step fails, the script will exit gracefully and provide an appropriate error message.

## Activating the Virtual Environment

To activate the virtual environment in the future, run:
```bash
source my_env/bin/activate
