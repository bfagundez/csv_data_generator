import click
from .csv_generator import default_generator


@click.command()
@click.option('--rows', default=5, help='Number of rows.')
@click.option('--cols', default=5, help='Number of cols.')
def start(rows, cols):
    click.echo(default_generator(rows, cols))
