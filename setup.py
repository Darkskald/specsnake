from setuptools import setup

setup(
    name='specsnake',
    version='0.0.0.1',
    packages=['specsnake'],
    url='https://github.com/Darkskald/specsnake',
    license='MIT',
    author='Darkskald',
    author_email='floriandavid.lange@web.de',
    description='',
    entry_points='''
        [console_scripts]
        cli=cli:hello
    ''',
)

# todo: install requirements with the help of this file
# todo: Dockerize