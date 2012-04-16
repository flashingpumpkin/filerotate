from setuptools import setup
from filerotate import __version__


setup(
    name='filerotate',
    version=__version__,
    author='Alen Mujezinovic',
    author_email='flashingpumpkin@gmail.com',
    packages=['filerotate'],
    description='Rotate filenames',
    long_description=open('README.rst').read(),
    entry_points = {
        'console_scripts': [
            'filerotate = filerotate:rotate',
        ]   
    }
)
