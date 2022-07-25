from setuptools import setup, find_packages
from typing import List



## Declaring variables for setup function

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR="M.SARITHA"
DESRCIPTION = "This is a first FSDS Nov batch Machine Learning Project"
PACKAGE = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()-> List[str]:
    """
     This function is going to return list of requirements mention in requirement.txt file
    
    return this function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file  
    """



    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return  requirement_file.readlines().remove("-e .")



setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESRCIPTION,
packages=find_packages(),
install_requires = get_requirements_list()

)