import setuptools

setuptools.setup(
    name="NPointController",
    version="0.0.1",
    author="Sebastian Jennen",
    author_email="sj@imagearts.de",
    description="TwoPointController",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['requests'],
    scripts=['NPointController.py']
)