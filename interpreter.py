import re

class Lexer:
    pass

class Tokenizer:
    def __init__(self):
        self.arithmetic_parameters = {
            '+' : 'PLUS',
            '-' : 'MINUS',
            '^' : 'POWER',
            '*' : 'TIMES',
            '|' : 'INTDEVISION',
            '/' : 'DEVISION',
            }
        self.logical_parameters = {
            '==' : 'EQUALS',
            '!=' : 'NEQUALS',
            '<=' : 'LTOE',
            '>=' : 'GTOE',
            '>' : 'GREATERTHAN',
            '<' : 'LESSTHAN',
            'wa' : 'AND',
            'ola' : 'OR'
        }
        self.special_characters_tokens = {
            '(' : 'LEFT_PAREN',
            ')' : 'RIGHT_PAREN',
            '[' : 'LEFT_BRACKET',
            ']' : 'RIGHT_BRACKET',
            '{' : 'LEFT_BRACE',
            '}' : 'RIGHT_BRACE',
            "'" : 'SINGLE_QUOTE',
            ':' : 'DO',
            }

        self.keywords = {
            'ma7ad' : 'WHILE',
            'likol' : 'FOR',
            'ida' : 'IF',
            'wila' : 'ELSE'
            } 

    def tokenize(self, line):
        tokens = []
        current_position = 0
        while current_position < len(line):
            # Check for whitespace and ignore it
            if re.match(r'\s', line[current_position]):
                current_position += 1
                continue

            # Check for comments and ignore them
            if re.match(r'#', line[current_position]):
                while current_position < len(line) and line[current_position] != '\n':
                    current_position += 1
                continue

            # Check for strings
            if re.match(r'"', line[current_position]):
                string_value = ''
                current_position += 1
                while current_position < len(line) and line[current_position] != '"':
                    string_value += line[current_position]
                    current_position += 1
                current_position += 1  # Skip the closing quote
                tokens.append(('STRING', string_value))
                continue

            # Check for numeric values
            if re.match(r'\d', line[current_position]):
                number_value = ''
                while current_position < len(line) and (re.match(r'\d', line[current_position]) or line[current_position] == '.'):
                    number_value += line[current_position]
                    current_position += 1
                tokens.append(('NUMBER', float(number_value) if '.' in number_value else int(number_value)))
                continue

            # Check for keywords
            for keyword, token_type in self.keywords.items():
                if re.match(fr'\b{re.escape(keyword)}\b', line[current_position:]):
                    token_value = keyword
                    tokens.append((token_type, token_value))
                    break
                continue
            
            for keyword, token_type in self.arithmetic_parameters.items():
                if re.match(re.escape(keyword), line[current_position]):
                    token_value = keyword
                    tokens.append((token_type, token_value))
                    break
                continue

            
            for keyword, token_type in self.special_characters_tokens.items():
                if re.match(re.escape(keyword), line[current_position]):
                    token_value = keyword
                    tokens.append((token_type, token_value))
                    break
                continue
                
            for keyword, token_type in self.logical_parameters.items():
                if re.match(re.escape(keyword), line[current_position:]):
                    token_value = keyword
                    tokens.append((token_type, token_value))
                    break
                continue
            current_position += 1
        
        return tokens

class Parser:
    def __init__(self, Lexer, Tokenizer, input, is_line):
        self.is_line = is_line
        self.Lexer = Lexer
        self.Tokenizer = Tokenizer
        self.input = input
        
    def parse(self):
        tokenizer = Tokenizer()
        if not self.is_line:
            with open(self.input, 'r') as f:
                code = f.read()
            for line in code.split('\n'):
                tokens = tokenizer.tokenize(line)
                print(tokens)
        else: 
            tokens = tokenizer.tokenize(self.input)
            print(tokens)
        