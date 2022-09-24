"""
Simple find and replace script targeting all files in the same directory with
a given extension
Originally created to fix a mistake en-masse when a set of test files was
created (manually) with one consistently incorrect tag
"""

import os

FILE_EXTENSION = ".xml"
REPLACE_INPUT = "abc"
REPLACE_OUTPUT = "xyz"

for file in os.listdir("."):
    if file.endswith(FILE_EXTENSION):
        with open(file, "w") as f:
            data = f.read()
            f.write(data.replace(REPLACE_INPUT, REPLACE_OUTPUT))
