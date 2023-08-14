class CSVGenerator:
    def __init__(self, rows: int = 5, cols: int = 5):
        self.rows = rows
        self.cols = cols

    def generate(self) -> str:
        """Generate a csv file with default values."""
        output = ""
        for header in range(self.cols):
            output += f"col{header+1}"
            if header != range(self.cols)[-1]:
                output += ","
        output += "\n"
        for x in range(self.rows):
            for y in range(self.cols):
                output += f"{y+1}"
                if y != range(self.cols)[-1]:
                    output += ","
            if x != range(self.rows)[-1]:
                output += "\n"
        return output
