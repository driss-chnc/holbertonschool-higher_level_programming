#!/usr/bin/env python3

"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it as data.json."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = list(csv.DictReader(file))

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file)

        return True
    except FileNotFoundError:
        return False
