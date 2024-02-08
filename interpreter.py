class Tokenizer:
    pass

class Lexer:
    def __init__(self, code):
        self.code = code
        
    def lex(self):
        lines = self.code.split("\n")
        print(lines)

class Parser:
    def __init__(self, Lexer, Tokenizer, file):
        self.Lexer = Lexer
        self.Tokenizer = Tokenizer
        self.file = file
        
    def parse(self):
        with open(self.file, 'r') as f:
            code = f.read()
        Lexer = self.Lexer(code)
        tokens = Lexer.lex()
        