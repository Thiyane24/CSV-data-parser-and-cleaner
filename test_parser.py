from data_parser.base import DataFile
from data_parser.csv_file import CSVFile 
from data_parser.json_file import JSONFile
from data_parser.tsv_file import TSVFile
csv = CSVFile("data/new_york_real_estate_2026_final.csv")

json= JSONFile("data/top100aitools2026.json")
tsv = TSVFile("data/file.tsv")
json.read()
json.clean()
json.validate()
json.summary()
print("\n")
csv.read()
csv.clean()
csv.validate()
csv.summary()
print("\n")
tsv.read()
tsv.clean()
tsv.validate()
tsv.summary()

