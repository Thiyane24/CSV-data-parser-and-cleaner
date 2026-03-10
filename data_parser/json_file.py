from data_parser.base import DataFile
import json

class JSONFile(DataFile):
    def __init__(self,filepath, delimiter = ';' ):
        super().__init__(filepath)
        self.delimiter = delimiter
        
    def read (self): 
        """Open the csv file and prints the rows """
        with open (self.filepath, "r") as read:
            self.data = json.load(read)
            if not isinstance(self.data, list):
                raise ValueError("Data must return a list")
        
        self.is_loaded= True

    def write(self,output_path):
        """Opens the csv file and writes the header and the rows of the file"""
        with open(output_path, "w") as write:
            json.dump(self.data,write, indent= 2)
                    
   