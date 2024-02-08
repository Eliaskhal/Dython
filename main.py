from sys import argv

from interpreter import Tokenizer
from interpreter import Lexer
from interpreter import Parser

if __name__ == "__main__":
    if len(argv) > 1:
        code = argv[1]
        parser = Parser(Lexer, Tokenizer, code, False)
        parser.parse()
    else: 
        while True:
            parser = Parser(Lexer, Tokenizer, input('>>> '), True)
            parser.parse()
    