import pathlib
from setuptools import find_packages, setup
import re

README = (pathlib.Path(__file__).parent / "README.md").read_text()

PACKAGE_NAME        = "opentele"
VERSION             = "1.0.9"
SOURCE_DIRECTORY    = "src"

# SOURCE_PACKAGE_REGEX = re.compile(rf'^{SOURCE_DIRECTORY}')
# srcPackages = find_packages(include=[SOURCE_DIRECTORY, f'{SOURCE_DIRECTORY}.*'])
# projectPackages = [SOURCE_PACKAGE_REGEX.sub(PACKAGE_NAME, name) for name in srcPackages]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="A python library created to make life easier for Telegram API Developers.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thedemons/opentele",
    author="thedemons",
    author_email="thedemons@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["opentele", "opentele.td", "opentele.tl"],
    # package_dir={PACKAGE_NAME: SOURCE_DIRECTORY},
    include_package_data=True,
    install_requires=["pyqt5", "telethon", "tgcrypto"],
)