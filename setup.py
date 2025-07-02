from setuptools import find_packages, setup
from typing import List

HYPEN_e_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''This function will return the list of requirments'''
    requirments = []
    with open(file_path,) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","")  for req in requirments]

        if HYPEN_e_DOT in requirments:
            requirments.remove(HYPEN_e_DOT)
    return requirments


setup(
    name='MLProject',
    version='0.0.1',
    author='Mohammad Arafah',
    authour_email = 'Mohammad_arafah@hotmail.com',
    packages= find_packages(),
    install_requires = get_requirments('requirements.txt')
)
