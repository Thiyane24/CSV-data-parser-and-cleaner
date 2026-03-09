class DataFile:
    def __init__(self, filepath,  data = None, is_loaded = False):
        """Initiates the class DataFile
        """
        self.filepath = filepath 
        self.data = data
        self.is_loaded = is_loaded 
        
    def __str__(self):
        """ shows the number of rows in the data we key in """
        rows = len(self.data) if self.data else "not loaded"
        return f"File: {self.filepath} | Rows: {rows}"
        
    
    def __repr__(self):
        """Returns the information about the DataFile
        """
        return f"DataFile(filepath = '{self.filepath}', loaded= {self.is_loaded})"
    
    def read(self):
        """Raises a NotImplementedError
        """
        raise NotImplementedError("Subclasses must implement read")
    
test= DataFile("top100_ai_tools_2026.csv")

print(test)

    