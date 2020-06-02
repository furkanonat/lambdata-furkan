# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-furkan", # the name that you will install via pip
    version="1.0",
    author="Furkan",
    author_email="your@email.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/furkanonat/lambdata-furkan",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)