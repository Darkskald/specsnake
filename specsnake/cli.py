import click

from specsnake.plotting import Plotter
from specsnake.tools import load_sfg


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option('--save/--no-save',  ' -s/-i', default=False)
def plot(filename, save):
    temp = Plotter([load_sfg()(filename)])
    if save:
        temp.save()
    else:
        temp.show()


