import click

from specsnake.tools import to_sfg, load_sfg


@click.command()
#@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    print(load_sfg()(name))

if __name__ == '__main__':
    hello()