from setuptools import find_packages,setup
from typing import List
Hyphen_E_Dot = "-e ."
def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list required packages we need
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n', '') for req in requirments]
        if Hyphen_E_Dot in requirments:
            requirments.remove(Hyphen_E_Dot)
    return requirments


setup(
name='ML_Project',
version='0.0.1',
description='Abhi ke lye kuch nhi',
packages=find_packages(),
install_requries = get_requirments('requirments.txt'),
)
