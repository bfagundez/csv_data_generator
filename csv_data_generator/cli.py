import click
from .csv_generator import CSVGenerator

@click.command()
@click.option('-r','--rows', default=5, help='Number of rows.')
@click.option('-c','--cols', default=5, help='Number of cols.')
@click.option('-fw','--fill-words',is_flag=True, default=False, help='Use random words to fill the csv.')
def start(rows, cols, fill_words):
    csv_generator = CSVGenerator(rows, cols, fill_words)
    click.echo(csv_generator.generate())
