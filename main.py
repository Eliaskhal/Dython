from translator import Translator, Parser

global_vars = {}
local_vars = {}

def main(code, is_line, global_vars, local_vars):
    parser = Parser(Translator, code, is_line)
    return parser.parse(global_vars, local_vars)

if __name__ == "__main__":
    from sys import argv
    
    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            code = f.read()
        main(code, False, {}, {})
    
    else: 
        while True:
            code = input('>>> ')
            global_vars, local_vars = main(code, True, global_vars, local_vars)