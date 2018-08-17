
from setuptools import setup, find_packages
from heimptui import __version__

setup(
    name='heimptui',
    version=__version__,

    url='https://www.github.com/withanage/heimptui',
    author='Dulip Withanage',
    author_email='dulip.withanage@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],

    install_requires=(
        'django >2.0',
    )
)