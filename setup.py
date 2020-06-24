
from setuptools import *

with open("README.md", "r") as fh:
    long_description = fh.read()

my_packages=find_packages()


setup(
  name = 'bitsbehumble',      
  packages = my_packages,  
  version = '0.5',      
  long_description=long_description,

  long_description_content_type="text/markdown", 
  author = 'Alya Gomaa',  
  url = 'https://github.com/AlyaGomaa/bitsbehumble', 
  download_url  = 'https://github.com/AlyaGomaa/bitsbehumble/releases/tag/v2.0',

  keywords = ['CTF', 'Converter'],  
  classifiers=[
    'Development Status :: 4 - Beta',    
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',  
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    
  ],
)
