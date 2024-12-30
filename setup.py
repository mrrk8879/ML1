from setuptools import find_packages, setup
from typing import List

# Constant for the "-e ." line in requirements.txt
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from the given file.
    """
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines and remove newline characters
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove whitespace/newlines

        # Remove "-e ." if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Define the setup configuration
setup(
    name='mlproject',  # Name of your project
    version='0.0.1',   # Version of your project
    author='Mohd Rihan',    # Your name or author of the project
    author_email='mrrk7977@gmail.com',  # Author's email
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=get_requirements('requirements.txt')  # Read dependencies
)
