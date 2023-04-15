import Quotes as Q
import csv
import random

class Quotes_Service(Q.Quotes):
    def __init__(self):
        super().__init__()
        
    def validate_quote(self, quote):
        if (quote == '' or quote == ' ' or quote == 'Enter quote here'):
            return False
        if (quote in [quote[1] for quote in self.quotes]):
            return False
        return True
    
    def add_quote(self, new_quote):
        if new_quote in [quote[1] for quote in self.quotes]:
            return False

        if not self.validate_quote(new_quote):
            return False

        next_number = max(int(quote[0]) for quote in self.quotes) + 1 if self.quotes else 1
        self.quotes.append([next_number, new_quote])

        with open(self.filename, 'w', newline='') as file:
            csv.writer(file).writerows([['Number', 'Quote']] + self.quotes)

        return True
        
    def add_quotes(self, new_quotes):
        for quote in new_quotes:
            self.add_quote(quote)
            
    def edit_quote(self, quote_old, new_quote):
        print(quote_old, new_quote)
        if not self.validate_quote(new_quote):
            return False
        for quote in self.quotes:
            if quote[1] == quote_old:
                quote[1] = new_quote

                with open(self.filename, 'w', newline='') as file:
                    csv.writer(file).writerows([['Number', 'Quote']] + self.quotes)
                return True
        return False
    
    def get_random_quote(self):
        return random.choice(self.quotes)[1]
    