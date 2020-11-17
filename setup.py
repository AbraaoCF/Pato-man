import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pato-man",
    version="0.4.4",
    author="Abraão Caiana de Freitas",
    author_email="abraao.freitas@ccc.ufcg.edu.br",
    description="Pac-man with ducks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbraaoCF/Pato-man",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pygame'
        ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'patoman=Patoman.menu:run'
            ]
        }
)
