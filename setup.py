from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    '''
    THIS WILL RETURN THE LIST OF REQUIREMENTS 
    '''
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            #process rach line
            for line in lines:
                requirement=line.strip()
                #ignore the -e.
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print('requirement file not found')

    return requirements_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Ayush Srivastava',
    author_email='ayushsrivastava0615@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),

)

