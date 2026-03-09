from base import DataFile
import csv

class CSVFile (DataFile):
    """ Initiates the class, with the parameters below and inherits from the DataFile class and takes attribute 'filepath' """
    def __init__(self,filepath, delimiter = ',' ):
        super().__init__(filepath)
        self.delimiter = delimiter
        
    def read (self):
        """Open the csv file and prints the rows """
        with open("Cars Fuel Effiency_ Benchmark Edition -.csv","r") as f:
            reader = csv.DictReader(f)
            row = [row for row in reader]
    
    def write(self,output_path):
        """Opens the csv file and writes the header and the rows of the file"""
        fieldnames = self.data[0].keys()
        with open("Cars Fuel Effiency_ Benchmark Edition -.csv", "w", newline ='') as write:
            writer = csv.DictWriter(writer, fieldnames = fieldnames)
            writer.writeheader("The first rows")
            writer.writerows(self.data)         
            
            
test1 = CSVFile("Cars Fuel Effiency_ Benchmark Edition -.csv")

test1.read()
test1.write()   