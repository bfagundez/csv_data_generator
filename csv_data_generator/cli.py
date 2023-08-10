import click
from .csv_generator import default_generator

@click.command()
@click.option('--rows', default=5, help='Number of rows.')
@click.option('--cols', default=5, help='Number of cols.')
#@click.option('--name', prompt='Your name',
#              help='The person to greet.')
def start(rows, cols):
    default_generator(rows, cols)


