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
        # Development status
        'Development Status :: 3 - Alpha',

        # Audience
        'Intended Audience :: Developers',

        # License
        'License :: OSI Approved :: MIT License',

        # Operating System
        'Operating System :: Microsoft :: Windows',

        # Version
        'Programming Language :: Python :: 3',
    ],

    keywords = "python macro development",

    install_requires = [
        'pypiwin32',
    ],
)
