# setup.py
from setuptools import setup, find_packages

setup(
    name='custom_transformer',
    version='0.1.0',
    description='Custom dataset loader with infant visual transformations',
    author='AM Pillai',
    author_email='amal.m.pillai@fau.de',
    packages=find_packages(),
    install_requires=[
        'torch',              # PyTorch
        'torchvision',        # torchvision (for datasets)
        'scikit-image',       # For image processing (e.g., rgb2gray)
        'numpy',              # For numerical computations
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
