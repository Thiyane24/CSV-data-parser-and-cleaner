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
    
    def validate(self):
        if self.data == None:
            return False
        if len(self.data) == 0:
            return False
        
        return True
    
    def clean(self):
        for row in self.data :
            for key, value in row.items():
                if isinstance(value,str):
                    row[key] = value.strip()
        
        self.data = [row for row in self.data if any(value for value in row.values())]
        
       
        self.data = [{(key.lower().replace(" ", "_").replace("-", "_") if isinstance(key,str) else key): value for key, value in row.items()} for row in self.data]
            
    
    def summary(self):
        print(f"Filepath: {self.filepath}")
        validate= self.validate()
        print("Valid: ",validate)
        print("Rows: ",len(self.data))
        print("Columns: ",list(self.data[0].keys()))
          
            


    