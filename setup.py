import pathlib
from setuptools import find_packages, setup
import re

README = (pathlib.Path(__file__).parent / "README.md").read_text()

PACKAGE_NAME = "opentele"
VERSION = "1.15"
SOURCE_DIRECTORY = "src"

with open("requirements.txt") as data:
    requirements = [
        line for line in data.read().split("\n") if line and not line.startswith("#")
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    license="MIT",
    description="A Python Telegram API Library for converting between tdata and telethon sessions, with built-in official Telegram APIs.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thedemons/opentele",
    author="thedemons",
    author_email="thedemons@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords=[
        "tdata",
        "tdesktop",
        "telegram",
        "telethon",
        "opentele",
    ],
    include_package_data=True,
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: SOURCE_DIRECTORY},
    install_requires=requirements,
)
