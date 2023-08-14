import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from csv_data_generator.csv_generator import CSVGenerator


def test_basic_output():
    assert CSVGenerator().generate()  == ''.join(("col1,col2,col3,col4,col5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n", 
                                          "1,2,3,4,5\n", 
                                          "1,2,3,4,5\n", 
                                          "1,2,3,4,5"))

def test_provided_only_rowcount():
    assert CSVGenerator(rows=10).generate() == ''.join(("col1,col2,col3,col4,col5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n",
                                          "1,2,3,4,5\n", 
                                          "1,2,3,4,5\n", 
                                          "1,2,3,4,5\n", 
                                          "1,2,3,4,5"))

def test_provided_only_colcount():
    assert CSVGenerator(cols=3).generate() == ''.join(("col1,col2,col3\n",
                                          "1,2,3\n",
                                          "1,2,3\n",
                                          "1,2,3\n",
                                          "1,2,3\n",
                                          "1,2,3"))

def test_provided_colcount():
    assert CSVGenerator(cols=10,rows=3).generate()  == ''.join(("col1,col2,col3,col4,col5,col6,col7,col8,col9,col10\n",
                                          "1,2,3,4,5,6,7,8,9,10\n",
                                          "1,2,3,4,5,6,7,8,9,10\n",
                                          "1,2,3,4,5,6,7,8,9,10"))

