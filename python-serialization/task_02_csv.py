#!/usr/bin/python3
"""Convert CSV file to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file into data.json."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
