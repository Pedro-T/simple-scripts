"""
Search for instances of a date in the format used by SWIFT MX
messages (YYYY-DD-MM), then replace it with the current date. Do so for all
files in the same directory ending with the same extension.
"""
import os
import re
import datetime

FILE_EXTENSION = ".xml"

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
for file in os.listdir("."):
    if file.endswith(FILE_EXTENSION):
        with open(file, "w") as f:
            f.write(re.sub(r"20[1-2]\d-[0-1]\d-[0-3]\d", current_date, f.read()))
