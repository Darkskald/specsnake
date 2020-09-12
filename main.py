# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pathlib import Path

from specsnake.plotting import Plotter
from specsnake.spectrum_factory import global_provider


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    sfg_factory = global_provider.provide_factory_by_name('sfg')
    lt_factory = global_provider.provide_factory_by_name('lt')
    print(sfg_factory.build_batch(Path('tests/data/test_sfg')))
    print(lt_factory.build_batch(Path('tests/data/test_lt')))
    Plotter(sfg_factory.build_batch(Path('tests/data/test_sfg'))).show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# pip install git+https://github.com/Darkskald/specsnake.git@master