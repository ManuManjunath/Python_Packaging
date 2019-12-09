from setuptools import setup, find_packages

exec(open("sample/version.py").read())
setup(
    description="sample PIP package",
    url="https://github.com/ManuManjunath/Python_Packaging",
    author="ManuManjunath",
    author_email="emailmanuman@gmail.com",
    version=__version__,
    packages=find_packages(),
    name="sample",
    install_requires=[],
)
