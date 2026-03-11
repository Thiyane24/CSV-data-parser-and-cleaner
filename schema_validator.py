from data_parser.csv_file import CSVFile
class SchemaValidator:
    def __init__(self,schema):
        self.schema = schema 
        
    def validate(self,data):
        """Validates the data, if the data is correct it returns an empty list [] else it returns a list of all the errors []"""
        if data == None:
            return []
        if len(data)== 0:
            return []
        
        error = []
        
        for index, row in enumerate(data):
            for column, expected_type in self.schema.items():
                value = row[column]
                if not isinstance(value, expected_type):
                    error.append({
                        "row": index,
                        "column": column,
                        "expected": expected_type,
                        "actual": type(value)
                    })
        return error
    
schema = {"beds": int, "sqft": float}
validator = SchemaValidator(schema)
csv = CSVFile("data/new_york_real_estate_2026_final.csv")
csv.read()
csv.clean()
print(csv.data[0].keys())
print("\n")
errors = validator.validate(csv.data)
print("\n")
print(errors)