from data_parser.base import DataFile
import csv

class CSVFile (DataFile):
    """ Initiates the class, with the parameters below and inherits from the DataFile class and takes attribute 'filepath' """
    def __init__(self,filepath, delimiter = ';' ):
        super().__init__(filepath)
        self.delimiter = delimiter
        
    def read (self):
        """Open the csv file and prints the rows """
        with open(self.filepath,"r") as f:
            reader = csv.DictReader(f, delimiter=self.delimiter)
            self.data = [row for row in reader]
            self.is_loaded = True

    def write(self,output_path):
        """Opens the csv file and writes the header and the rows of the file"""
        fieldnames = self.data[0].keys()
        with open(output_path, "w", newline ='') as write:
            writer = csv.DictWriter(write, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(self.data)         
            
            
test1 = CSVFile("data/file.tsv")

test1.read()
test1.write("file.tsv")   