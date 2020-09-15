from setuptools import setup, find_packages

setup(
    name='specsnake',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/Darkskald/specsnake',
    license='MIT',
    author='Darkskald',
    author_email='floriandavid.lange@web.de',
    description='',
    include_package_data=True,
    install_requires=[
        'Click',
        'matplotlib>=3.3.1',
        'numpy>=1.18.5',
        'pandas>=1.1.1',
        'peakutils>=1.3.3',
        'scipy>=1.5.2',
        'setuptools>=49.6.0',
        'click>=7.1.2',
        'sphinx-autodoc-typehints',
    ],
    entry_points={
        'console_scripts':
        ['specsnake=specsnake.cli:cli']}
)
# todo: Dockerize