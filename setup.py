from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    req_list:List[str]=[]
    try: 
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()
            
            for line in lines:
                req=line.strip()
                ## ignore empty lines and -e.
                if req and req != '-e .':
                    req_list.append(req)
                    
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return req_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Long HoDac",
    author_email="long110404@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
    