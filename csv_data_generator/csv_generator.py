import click

def default_generator(rows: int = 5, cols: int = 5) -> str:
    """Generate a csv file with default values."""
    output = ""
    for header in range(cols):
        output += f"col{header},"
    output += "\n"
    for x in range(rows):
        for y in range(cols):
            output += f"{y},"
        output += "\n"
    return output

