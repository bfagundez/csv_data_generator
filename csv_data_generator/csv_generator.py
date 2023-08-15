import os

class CSVGenerator:
    def __init__(self, rows: int = 5, cols: int = 5):
        self.rows = rows
        self.cols = cols
        #self.words = open(self.get_words_path).read().splitlines()
        #print(self.words)
        print('this is the current path:')
        current_path = os.path.dirname(os.path.realpath('__file__'))
        print(current_path)

    def get_words_path(self) -> str:
        print('this is the current path:')
        current_path = os.path.dirname(os.path.realpath('__file__'))
        print(current_path)
        #current_path + "/dict/words.txt"
        return current_path
    def generate(self) -> str:
        """Generate a csv file with default values."""
        return self.headerGenerator() + self.rowsGenerator()
   
    def headerGenerator(self) -> str:
        output = ""
        for header in range(self.cols):
            output += f"col{header+1}"
            if header != range(self.cols)[-1]:
                output += ","
        output += "\n"
        return output
    
    def rowsGenerator(self) -> str:
        """Generate rows with default values."""
        output = ""
        for x in range(self.rows):
            lastRow = x != range(self.rows)[-1]
            output += self.rowGenerator(lastRow)
        return output

    def rowGenerator(self,lastRow = False) -> str:
        """Generate a row with default values."""
        output = ""
        for y in range(self.cols):
            output += f"{y+1}"
            if y != range(self.cols)[-1]:
                output += ","
        if lastRow:
            output += "\n"
        return output
