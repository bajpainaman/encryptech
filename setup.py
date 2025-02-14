from setuptools import setup, find_packages

setup(
    name="encryptech",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A placeholder Python package for Encryptech API interactions",
    url="https://github.com/yourusername/encryptech",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
