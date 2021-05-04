from setuptools import setup, find_packages

setup(
    name="mm_ide",
    author="Manas Mishra",
    author_email="manas.m22@gmail.com",
    description="An ide made using python",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manasm11/mm-ide",
    version="0.0.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
