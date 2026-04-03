from setuptools import setup, find_packages

setup(
    name = "mypackage",
    version = "0.1",
    packages = find_packages(exclude=["tests"]),
    license = "MIT",
    description = "EDSA example package",
    long_description = open("Readme.MD"),
    install_requires = ["Numpy"],
    url = "Https//:github.com/alred_142/mypackage",
    author ="alfred",
    author_email = "wawerualfred14@gmail.com"
)
