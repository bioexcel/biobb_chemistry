import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_chemistry",
    version="2.0.2",
    author="Biobb developers",
    author_email="genis.bayarri@irbbarcelona.org",
    description="Biobb_chemistry is the Biobb module collection to perform chemistry over molecular dynamics simulations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_chemistry",
    project_urls={
        "Documentation": "https://biobb-chemistry.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['docs', 'test',]),
    install_requires=['biobb_common==2.0.1'],
    python_requires='==3.6.*',
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)
