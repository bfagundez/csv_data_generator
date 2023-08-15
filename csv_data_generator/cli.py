import click
from .csv_generator import CSVGenerator

@click.command()
@click.option('--rows', default=5, help='Number of rows.')
@click.option('--cols', default=5, help='Number of cols.')
@click.option('--fill-words', default=5, help='Use random words to fill the csv.')
def start(rows, cols):
    csv_generator = CSVGenerator(rows, cols, fill_words)
    click.echo(csv_generator.generate())
