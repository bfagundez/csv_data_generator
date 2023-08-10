import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from csv_data_generator.csv_generator import default_generator

def test_basic_output():
    assert default_generator() == "col0,col1,col2,col3,col4,\n0,1,2,3,4,\n0,1,2,3,4,\n0,1,2,3,4,\n0,1,2,3,4,\n0,1,2,3,4,\n"
