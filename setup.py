from setuptools import setup, find_packages
from typing import List
from pathlib import Path

from my_pip_package import __version__

extra_math = [
    'returns-decorator',
]

extra_bin = [
    *extra_math,
]

extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

def get_install_requires() -> List[str]:
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets


setup(
    name='my_pip_package',
    version=__version__,
    description='A tutorial for creating pip packages.',

    url='https://github.com/rileyhun/tutorial-pip-package/',
    author='Riley Hun',
    author_email='riley.hun@autodesk.com',

    packages=find_packages(exclude=['tests', 'tests.*']),

    install_requires=get_install_requires(),

    extras_require={
        'math': extra_math,

        'bin': extra_bin,

        'test': extra_test,
        'dev': extra_dev,

        'ci': extra_ci,
    },

    entry_points={
        'console_scripts': [
            'add=my_pip_package.math:cmd_add',
        ],
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
