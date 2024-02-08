import re

class Lexer:
    pass

class Tokenizer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.arithmetic_parameters = {
            '+' : 'PLUS',
            '-' : 'MINUS',
            #'**' : 'POWER',
            '*' : 'TIMES',
            #'//' : 'INTDEVISION',
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
            '\t' : 'TAB'
            }

        self.keywords = {
            'ma7ad' : 'WHILE',
            'likol' : 'FOR',
            'ida' : 'IF',
            'wila' : 'ELSE'
            } 

    def tokenize(self):
        tokens = []
        for line in self.source_code.split("\n"):
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
                    while current_position < len(line) and re.match(r'\d', line[current_position]):
                        number_value += line[current_position]
                        current_position += 1
                    tokens.append(('NUMBER', int(number_value)))
                    continue

                # Check for keywords
                for keyword, token_type in self.keywords.items():
                    if re.match(fr'\b{re.escape(keyword)}\b', line[current_position:]):
                        token_value = keyword
                        current_position += len(keyword)
                        tokens.append((token_type, token_value))
                        break
                    continue
                
                for keyword, token_type in self.arithmetic_parameters.items():
                    if re.match(re.escape(keyword), line[current_position]):
                        token_value = keyword
                        current_position += len(keyword)
                        tokens.append((token_type, token_value))
                        break
                    continue

                
                for keyword, token_type in self.special_characters_tokens.items():
                    if re.match(re.escape(keyword), line[current_position]):
                        token_value = keyword
                        current_position += len(keyword)
                        tokens.append((token_type, token_value))
                        break
                    continue
                    
                for keyword, token_type in self.logical_parameters.items():
                    if re.match(re.escape(keyword), line[current_position:]):
                        token_value = keyword
                        current_position += len(keyword)
                        tokens.append((token_type, token_value))
                        break
                    
                current_position += 1

            tokens.append(('\n', 'NEWLINE'))
        
        return tokens

class Parser:
    def __init__(self, Lexer, Tokenizer, file):
        self.Lexer = Lexer
        self.Tokenizer = Tokenizer
        self.file = file
        
    def parse(self):
        with open(self.file, 'r') as f:
            code = f.read()
        tokenizer = self.Tokenizer(code)
        tokens = tokenizer.tokenize()
        print(tokens)
        