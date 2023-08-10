import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from csv_data_generator.csv_generator import default_generator


def test_basic_output():
    assert default_generator(
    ) == "col1,col2,col3,col4,col5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5"


def test_provided_only_rowcount():
    assert default_generator(
        10
    ) == "col1,col2,col3,col4,col5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5\n1,2,3,4,5"


def test_provided_only_colcount():
    assert default_generator(
        cols=3) == "col1,col2,col3\n1,2,3\n1,2,3\n1,2,3\n1,2,3\n1,2,3"


def test_provided_colcount():
    assert default_generator(
        3, 10
    ) == "col1,col2,col3,col4,col5,col6,col7,col8,col9,col10\n1,2,3,4,5,6,7,8,9,10\n1,2,3,4,5,6,7,8,9,10\n1,2,3,4,5,6,7,8,9,10"
