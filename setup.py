import io
import os
from setuptools import find_packages, setup

def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="valaya",
    version=read("valaya", "VERSION"),
    description="A secure and customizable cloud storage system.",
    url="https://github.com/sakshine108/valaya/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="sakshine108",
    packages=find_packages(),
    package_data={"valaya": ["config.yaml"]},
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["valaya = valaya.valaya_cli:main"]
    },
)