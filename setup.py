from setuptools import setup, find_packages

setup(
    name='specsnake',
    version='0.0.0.7',
    packages=find_packages(),
    url='https://github.com/Darkskald/specsnake',
    license='MIT',
    author='Darkskald',
    author_email='floriandavid.lange@web.de',
    description='',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts':
        ['specsnake=specsnake.cli:cli']}
)

# todo: install requirements with the help of this file
# todo: Dockerize