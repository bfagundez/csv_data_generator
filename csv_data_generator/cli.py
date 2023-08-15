import click
from .csv_generator import CSVGenerator


@click.command()
@click.option('--rows', default=5, help='Number of rows.')
@click.option('--cols', default=5, help='Number of cols.')
def start(rows, cols):
    csv_generator = CSVGenerator(rows, cols)
    click.echo(csv_generator.generate())
