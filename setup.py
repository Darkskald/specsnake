from setuptools import setup, find_packages

setup(
    name='specsnake',
    version='0.0.0.4',
    packages=find_packages(),
    url='https://github.com/Darkskald/specsnake',
    license='MIT',
    author='Darkskald',
    author_email='floriandavid.lange@web.de',
    description='',
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts':
        ['specsnake=specsnake.cli:hello']}
)

# todo: install requirements with the help of this file
# todo: Dockerize