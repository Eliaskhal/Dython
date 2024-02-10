from sys import argv

from translator import Translator
from translator import Parser

global_vars = {}
local_vars = {}

if __name__ == "__main__":
    if len(argv) > 1:
        code = argv[1]
        parser = Parser(Translator, code, False)
        parser.parse({}, {})
    else: 
        while True:
            parser = Parser(Translator, input('>>> '), True)
            global_vars, local_vars = parser.parse(global_vars, local_vars)
    