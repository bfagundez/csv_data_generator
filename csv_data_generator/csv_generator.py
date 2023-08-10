import click


def default_generator(rows: int = 5, cols: int = 5) -> str:
    """Generate a csv file with default values."""
    output = ""
    for header in range(cols):
        output += f"col{header+1}"
        if header != range(cols)[-1]:
            output += ","
    output += "\n"
    for x in range(rows):
        for y in range(cols):
            output += f"{y+1}"
            if y != range(cols)[-1]:
                output += ","
        if x != range(rows)[-1]:
            output += "\n"
    return output
