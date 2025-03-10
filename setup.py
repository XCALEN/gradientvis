from setuptools import setup, find_packages

setup(
    name="gradientvis",
    version="0.1.0",
    description="A Python library for visualizing neural network gradients.",
    author="Arcoson",
    author_email="hylendust@gmail.com",
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "matplotlib",
        "opencv-python"
    ],
)
