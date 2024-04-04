
from setuptools import setup, find_packages
from office-cli.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='office-cli',
    version=VERSION,
    description='Office CLI automates office tasks',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Aurghyadip Kundu',
    author_email='aurghya.blog@gmail.com',
    url='https://github.com/johndoe/myapp/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'office-cli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        office-cli = office-cli.main:main
    """,
)
