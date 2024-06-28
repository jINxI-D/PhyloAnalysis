from setuptools import setup, find_packages

setup(
    name="PhyloAnalysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "PhyloAnalysis=phyloanalysis.main:run_phyloanalysis",
        ],
    },
    author="Jinxi Dong",
    author_email="jinxi001@e.ntu.edu.sg",
    description="A tool for phylogenetic analysis and representative sequence extraction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jINxI-D/PhyloAnalysis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
