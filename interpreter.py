class Tokenizer:
    pass

class Lexer:
    pass

class Parser:
    def __init__(self, file):
        self.file = file
        
    def parse(self):
        with open(self.file, 'r') as f:
            code = f.read()
        print(code)