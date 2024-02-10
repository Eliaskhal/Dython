import re

class Translator:
    def __init__(self):
        self.keywords = {
            'importer': 'import',
            'de': 'from',
            'comme': 'as',
            'def': 'def',
            'classe': 'class',
            'retour': 'return',
            'si': 'if',
            'sinon': 'else',
            'sinonsi': 'elif',
            'tantque': 'while',
            'pour': 'for',
            'dans': 'in',
            'arret': 'break',
            'continuer': 'continue',
            'passer': 'pass',
            'Vrai': 'True',
            'Faux': 'False',
            'Aucun': 'None',
            'et': 'and',
            'ou': 'or',
            'pas': 'not',
            'est': 'is',
            'essayer': 'try',
            'sauf': 'except',
            'enfin': 'finally',
            'lever': 'raise',
            'affirmer': 'assert',
            'avec': 'with',
            'lambda': 'lambda',
            'imprimer' : 'print',
            'entrer' : 'input'
            }


    def translate(self, code):
        py_code = ''
        current_position = 0
        while current_position < len(code):
            # Check for keywords
            for keyword, translation in self.keywords.items():
                if re.match(fr'\b{re.escape(keyword)}\b', code[current_position:]):
                    py_code += translation
                    current_position += len(keyword)
                    break
                continue
            
            py_code += code[current_position]
            current_position += 1
        
        return py_code
    
    
    

class Parser:
    def __init__(self, Translator, input, is_line):
        self.is_line = is_line
        self.Translator = Translator
        self.input = input
        
    def parse(self):
        translator = Translator()
        if not self.is_line:
            with open(self.input, 'r') as f:
                code = f.read()
            with open(self.input[:self.input.find('.')] + '.py', 'w') as new_f:
                new_code = translator.translate(code)
                new_f.write(new_code)
        else: 
            new_line = translator.translate_line(self.input)
            print(new_line)
            exec(new_line)
        