import click

def default_generator(rows: int = 5, cols: int = 5) -> None:
    for header in range(cols):
        click.echo(f"col{header},", nl=False)
    click.echo("")
    for x in range(rows):
        for y in range(cols):
            click.echo(f"{y},", nl=False)
        click.echo("")

