from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    description="EDSA example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["numpy"],
    url="https://github.com/alfred_142/mypackage",
    author="alfred",
    author_email="wawerualfred14@gmail.com",
    python_requires=">=3.7",
)