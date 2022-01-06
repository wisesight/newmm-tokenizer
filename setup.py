from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="newmm_tokenizer",
    version="0.2.2",
    author="WISESIGHT Product Development",
    author_email="tequila@wisesight.com",
    description="Standalone Dictionary-based, Maximum Matching + Thai Character Cluster (newmm) tokenizer extracted from PyThaiNLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wisesight/newmm-tokenizer",
    packages=find_packages(),
    package_data={
        "newmm_tokenizer": ['README.md', 'words_th.txt']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
)
