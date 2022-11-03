from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This fn will return the list of requiremnets
    """
    requirement_list:List[str]= []

    # Write fn to read from requiremnets.txt file and convert into a list.  
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Hima",
    author_email="himathaivalappil@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()     #["pymongo==4.2.0"],
)

# to run python setup.py install