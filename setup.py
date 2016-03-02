from setuptools import setup, find_packages
from typy import __version__

setup(
    name = 'typy',
    version = __version__,

    description = "Windows utility for macro design",
    long_description = "A module for windows users that will aid in the automation of mouse movements and typing",

    # Project homepage
    url = "http://github.com/ewildawe/typy",

    # Author details
    author = 'http://github.com/ewildawe',
    author_email = 'ewildawe@gmail.com',

    license = 'MIT',
    packages = find_packages(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Licence :: MIT Licence',
        'Programming Language :: Python :: 3.x',
    ],

    keywords = "python macro development",

    install_requires = [
        'pypiwin32',
    ],
)
