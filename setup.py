import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pato-man", # Replace with your own username
    version="0.4.1",
    author="Abraão Caiana de Freitas",
    author_email="abraao.freitas@ccc.ufcg.edu.br",
    description="Pac-man with ducks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbraaoCF/Pato-man",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
