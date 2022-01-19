import pathlib
from setuptools import find_packages, setup
import re

README = (pathlib.Path(__file__).parent / "README.md").read_text()

PACKAGE_NAME        = "opentele"
VERSION             = "1.0.9"
SOURCE_DIRECTORY    = "src"

with open("requirements.txt") as data:
    requirements = [
        line for line in data.read().split("\n")
        if line and not line.startswith("#")
    ]

setup(

    name=PACKAGE_NAME,
    version=VERSION,
    license="MIT",

    description="A python library created to make life easier for Telegram API Developers.",
    long_description=README,
    long_description_content_type="text/markdown",
    
    url="https://github.com/thedemons/opentele",
    author="thedemons",
    author_email="thedemons@gmail.com",
    
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    
    kerwords=[
        "tdata",
        "tdesktop",
        "telegram",
        "telethon",
        "opentele",
    ],
    
    packages=["opentele", "opentele.td", "opentele.tl"],
    package_dir={'opentele': 'src'},
    include_package_data=True,
    install_requires=requirements,
)