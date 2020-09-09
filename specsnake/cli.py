import os
from pathlib import Path

import click

from specsnake.plotting import Plotter
from specsnake.spectrum_factory import global_provider


@click.group()
def cli():
    pass

"""
@cli.command()
@click.argument('filename')
@click.option('--save/--no-save',  ' -s/-i', default=False)
def plot(filename, save):
    temp = Plotter([load_sfg()(filename)])
    if save:
        temp.save()
    else:
        temp.show()
"""
# todo: pass command line argument
@cli.command()
@click.argument('stype')
@click.option('--save/--no-save',  ' -s/-i', default=False)
def plotall(stype, save):
    # todo: custom error if desired spec not available and init fails
    factory = global_provider.provide_factory_by_name(stype)
    path = Path(os.getcwd())
    specs = factory.build_batch(path)
    p = Plotter(specs)
    if save:
        p.save()
    else:
        p.show()

