from setuptools import setup

setup(
    name = 'PwAES',
    version = '1.0.0',
    description = 'password based AES encryption of text/ text files',
    url = 'https://github.com/bobGSmith/PwAES',
    author = 'Bob G Smith',
    author_email = 'bobbyatopk@gmail.com',
    license = 'MIT',
    packages = ['PwAES'],
    install_requires = ["pwinput","pycryptodome"],
    classifiers = ['Development Status :: 2 - Pre-Alpha','Intended Audience:: Developers','License :: MIT','Operating System :: OS Independent','Programming Language :: Python :: 3.8']
)