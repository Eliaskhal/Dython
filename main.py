from sys import argv

from interpreter import Tokenizer
from interpreter import Lexer
from interpreter import Parser

if __name__ == "__main__":
    Parser = Parser(Lexer, Tokenizer, argv[1])
    Parser.parse()