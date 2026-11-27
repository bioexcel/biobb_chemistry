import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_chemistry",
    version="5.3.2",
    author="Biobb developers",
    author_email="genis.bayarri@irbbarcelona.org",
    description="Biobb_chemistry is the Biobb module collection to perform chemistry over molecular dynamics simulations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_chemistry",
    project_urls={
        "Documentation": "https://biobb-chemistry.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/",
    },
    packages=setuptools.find_packages(exclude=["docs", "test"]),
    package_data={"biobb_chemistry": ["py.typed"]},
    install_requires=["biobb_common==5.3.1"],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "acpype_params_ac = biobb_chemistry.acpype.acpype_params_ac:AcpypeParamsAC.main",
            "acpype_params_cns = biobb_chemistry.acpype.acpype_params_cns:AcpypeParamsCNS.main",
            "acpype_params_gmx_opls = biobb_chemistry.acpype.acpype_params_gmx_opls:AcpypeParamsGMXOPLS.main",
            "acpype_params_gmx = biobb_chemistry.acpype.acpype_params_gmx:AcpypeParamsGMX.main",
            "acpype_convert_amber_to_gmx = biobb_chemistry.acpype.acpype_convert_amber_to_gmx:AcpypeConvertAMBERtoGMX.main",
            "reduce_add_hydrogens = biobb_chemistry.ambertools.reduce_add_hydrogens:ReduceAddHydrogens.main",
            "reduce_remove_hydrogens = biobb_chemistry.ambertools.reduce_remove_hydrogens:ReduceRemoveHydrogens.main",
            "babel_add_hydrogens = biobb_chemistry.babelm.babel_add_hydrogens:BabelAddHydrogens.main",
            "babel_convert = biobb_chemistry.babelm.babel_convert:BabelConvert.main",
            "babel_minimize = biobb_chemistry.babelm.babel_minimize:BabelMinimize.main",
            "babel_remove_hydrogens = biobb_chemistry.babelm.babel_remove_hydrogens:BabelRemoveHydrogens.main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
)
