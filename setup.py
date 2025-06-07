from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:  
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any comments and empty lines.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='neha',
    author_email='18.prasadneha@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A small ML project',
)