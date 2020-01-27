
from setuptools import setup, find_packages
from ompdjango import __version__

setup(
    name='ompdjango',
    version=__version__,

    url='https://www.github.com/withanage/ompdjango',
    author='Dulip Withanage',
    author_email='dulip.withanage@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],

    install_requires=(
        'django >2.0',
    )
)