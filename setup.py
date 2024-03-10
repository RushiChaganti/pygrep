from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '1.0'
DESCRIPTION = 'A Python tool similar to grep for searching patterns in files.'
LONG_DESCRIPTION = 'A command-line tool for searching patterns in files and directories.'

# Setting up
setup(
    name="pygrep",
    version=VERSION,
    author="Rushi Chaganti",
    author_email="<rushi2004rushi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],  # Adjust dependencies if needed
    keywords=['python', 'grep', 'search', 'pattern', 'files', 'directories'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
