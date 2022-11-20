from setuptools import setup,find_packages
from typing import List

#Declaring variable for setup function
PROJECT_NAME="housing_predictior"
VERSION="0.0.2"
AUTHOR="Renga Rajan"
DESCRIPTION="This is my second ML Project"
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description:This function is going to return list of requirements 
    mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)