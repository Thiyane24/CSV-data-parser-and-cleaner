# CSV Data Parser & Cleaner

A file-handling system built in Python using Object-Oriented 
Programming principles. Reads, validates, cleans, and exports 
structured data from multiple file formats.

## Project Structure

project-01-data-parser/
├── data_parser/
│   ├── __init__.py
│   ├── base.py        # DataFile base class
│   ├── csv_file.py    # CSVFile subclass
│   ├── json_file.py   # JSONFile subclass
│   └── tsv_file.py    # TSVFile subclass
├── data/              # Sample datasets
├── output/            # Cleaned output files
└── test_parser.py     # Integration tests

## Features

- Reads CSV, JSON, and TSV files into a unified structure
- Cleans data: strips whitespace, removes blank rows, 
  normalises column names to snake_case
- Validates data before processing
- Writes cleaned output to a new file
- Summary reporting: filepath, row count, column names

## OOP Concepts Used

- Inheritance — CSVFile, JSONFile, TSVFile extend DataFile
- Polymorphism — same interface works across all file types
- Encapsulation — file state managed inside class attributes
- Abstract methods — base class enforces subclass contracts

## How to Run
```python
from data_parser.csv_file import CSVFile

csv = CSVFile("data/your_file.csv")
csv.read()
csv.clean()
csv.validate()
csv.summary()
csv.write("output/cleaned.csv")

```

## Tech Stack
- Python 3.10+
- Standard library only: csv, json, os

## Context
This is Project 1 of a 7-project Data Engineering learning 
path focused on building DE fundamentals through OOP Python.
