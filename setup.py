# Any python project , set up file is required at first. We want our code to ge import in some other file
# Convert code into library using setup.py file
# Distribution of source code, we can use our code anywhere
# Create requirement.txt file where all the libraries will be present for installation
# And mention -e . for editable extensin in the requirements.txt file
from setuptools import find_packages, setup  
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()-> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name = "sensor", # name of the project
    version = "0.0.2", #keep changing version after modifying
    author = "ineuron", #author name
    author_email= "subhashdixit17@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(), # Provide list of libraries needed
)

