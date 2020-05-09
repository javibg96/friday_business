from setuptools import setup, find_packages
import os

friday_packages = [f"friday_business.{package}" for package in find_packages(where=os.path.join(os.path.dirname(__file__), 'friday_business'))]
friday_packages.append("friday_business")

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt.txt')) as f:
    requirements = [line.strip() for line in f.read().splitlines()]

setup(
    name='fridaybusiness',
    version=".0",
    packages=friday_packages,
    include_package_data=True,
    package_dir={"friday_business"},
    url='https://github.com/javibg96/friday_business/',
    author='Javier Blasco',
    install_requires=requirements,
    author_email="blascogarcia.javier@outlook.com",
    description='this is a project for testing diferent APIs and protocols'
)

