from setuptools import setup, find_packages
setup(
    name="bristoSOFTContacts",
    version="0.1",
    author="Kirk A Jackson",
    author_email="jacksonirka@bristosoft.org",
    url="https://bitbucket.org/bristolians/bristosoftcontacts/src/master/", 
    packages=find_packages(),
    classifiers=["Programming Language:: Python :: 3", 
                        "License :: OSI Approved :: MIT License", 
                        "Operating System :: OS Independent", 
                        ], 
    python_requires='>=3.6', 
    scripts=['main.py'],
)

