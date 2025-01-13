import json

class JsonReader():
    def __init__(self):
        self.data = None

    def open_file(self, file_name: str):
        with open(file_name, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
    
    def print_data(self):
        print(self.data)
    
    

def main():
    file_name = "sample-json-4.json"
    reader = JsonReader()
    reader.open_file(file_name)
    reader.print_data()

try:
    main()
except FileNotFoundError:
    print('Error: file not found')
except json.decoder.JSONDecodeError:
    print('Error: cannot open file')