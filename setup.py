import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_chemistry",
    version="3.8.0",
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
    packages=setuptools.find_packages(exclude=['docs', 'test']),
    install_requires=['biobb_common==3.8.1'],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "acpype_params_ac = biobb_chemistry.acpype.acpype_params_ac:main",
            "acpype_params_cns = biobb_chemistry.acpype.acpype_params_cns:main",
            "acpype_params_gmx_opls = biobb_chemistry.acpype.acpype_params_gmx_opls:main",
            "acpype_params_gmx = biobb_chemistry.acpype.acpype_params_gmx:main",
            "reduce_add_hydrogens = biobb_chemistry.ambertools.reduce_add_hydrogens:main",
            "reduce_remove_hydrogens = biobb_chemistry.ambertools.reduce_remove_hydrogens:main",
            "babel_add_hydrogens = biobb_chemistry.babelm.babel_add_hydrogens:main",
            "babel_convert = biobb_chemistry.babelm.babel_convert:main",
            "babel_minimize = biobb_chemistry.babelm.babel_minimize:main",
            "babel_remove_hydrogens = biobb_chemistry.babelm.babel_remove_hydrogens:main"
        ]
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)
