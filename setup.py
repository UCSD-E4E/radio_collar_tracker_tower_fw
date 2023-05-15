from setuptools import setup, find_packages
import RCTTower

setup(
    name='RCTTower',
    version=RCTTower.__version__,
    author='UCSD Engineers for Exploration',
    author_email='e4e@eng.ucsd.edu',
    entry_points={
        'console_scripts': [
            'rct_tower = RCTTower.main:main'
        ]
    },
    packages=find_packages(),
    install_requires=[
        "pyserial",
        "appdirs",
    ]
)