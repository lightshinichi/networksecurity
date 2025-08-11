from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements"""
    requirements_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from requirements.txt
            
            #process the requirements and remove any empty lines and -e.
        
        
            lines = file.readlines()
            for line in lines:
                requirements= line.strip()
                if requirements and requirements!='-e .':
                    requirements_list.append(requirements)
                    
    except FileNotFoundError:
        print("requirements.txt file not found. Returning an empty list.")
    return requirements_list

setup(
    name='NetworkSecurityProject',
    version='0.0.1',
    author='Naveen Prakash',
    author_email="rnaveenprakash25@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
