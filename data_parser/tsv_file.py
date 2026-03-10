from data_parser.csv_file import CSVFile

class TSVFile(CSVFile):
    def __init__(self,filepath, delimiter = "\t"):
        super().__init__(filepath,delimiter )
        self.delimiter = delimiter
    
