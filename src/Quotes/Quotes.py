import csv

class Quotes:
    # Konstruktor
    def __init__(self):
        self.filename = 'Quotes/Quotes.csv'
        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)  # Skip header row
            self.quotes = [[int(row[0]), row[1]] for row in csvreader]
    
    # Getter
    def get_quote(self, index):
        return self.quotes[index][1]
    