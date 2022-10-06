"""
Very basic reconciler for two csv files where reconcilement is based on a
single column of unique values.
"""

import csv
from sys import exit
from os.path import exists
import copy

FILE1_NAME = "file_a.csv"
FILE2_NAME = "file_b.csv"
KEY_COLUMN = "Id Number"

if not exists(FILE1_NAME) or not exists(FILE2_NAME):
    print("Comparison sheets not found")
    exit(1)

entries = {}
matched_counter = 0
with open(FILE1_NAME) as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    for entry in reader:
        entries[entry[KEY_COLUMN].strip()] = copy.copy(entry)

with open(FILE2_NAME) as f:
    reader = csv.DictReader(f)
    for entry in reader:
        key_id = entry[KEY_COLUMN]
        if key_id in entries:
            entries.pop(key_id)
            matched_counter += 1
        else:
            entries[key_id] = copy.copy(entry)

with open("output.csv", "w", newline="") as out:
    writer = csv.DictWriter(out, fieldnames=headers,
                            dialect="excel", delimiter=",",
                            quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in entries.values():
        writer.writerow(row)
print(f"Match: {matched_counter}\nMismatch: {len(entries)}\nCheck output.csv")
