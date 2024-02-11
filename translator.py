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
            'entrer' : 'input',
            'quitter' : 'exit',
            'plage' : 'range',
            'ouvrir': 'open',
            'fermer': 'close',
            'lire': 'read',
            'ecrire': 'write',
            'append': 'append',
            'longeur': 'len',
            'chaine': 'str',
            'flottant': 'float',
            'liste': 'list',
            'tout': 'all',
            'nimporte': 'any',
            'filtrer': 'filter',
            'somme': 'sum',
            'trier': 'sorted',
            'recherche': 'search',
            'remplacer': 'replace',
            'diviser': 'split',
            'joindre': 'join',
            'formater': 'format',
            'zip': 'zip',
            'abs': 'abs',
            'arrondir': 'round',
            'fichier': 'dir',
            'id': 'id',
            'ordre': 'ord',
            'lettre': 'chr',
            'soi' : 'self',
            'temps' : 'time', 
            'dormir' : 'sleep'
            }


    def translate(self, code):
        py_code = ''
        current_position = 0
        inside_string1 = False
        inside_string2 = False
        inside_comment = False
        while current_position < len(code):
            # Check for quotes and toggle inside_string
            if code[current_position] == '"':
                inside_string1 = not inside_string1
            if code[current_position] == "'":
                inside_string1 = not inside_string1

            # Check for comments and toggle inside_comment
            if code[current_position] == '#' and not inside_string1 and not inside_string2:
                while current_position < len(code) and code[current_position] != '\n':
                    current_position += 1
                continue

            # Check for keywords if not inside string or comment
            if not inside_string1 and not inside_string2 and not inside_comment:
                for keyword, translation in self.keywords.items():
                    if re.match(fr'\b{re.escape(keyword)}\b', code[current_position:]):
                        py_code += translation
                        current_position += len(keyword)
                        break
                else:
                    py_code += code[current_position]
                    current_position += 1
            else:
                py_code += code[current_position]
                current_position += 1

        return py_code

class Parser:
    def __init__(self, Translator, input, is_line):
        self.is_line = is_line
        self.Translator = Translator
        self.input = input
        
    def parse(self, global_vars, local_vars):
        translator = Translator()
        if not self.is_line:
            with open(self.input, 'r') as f:
                code = f.read()
            new_code = translator.translate(code)
            # with open('new_code.py', 'w') as f: f.write(new_code)
            exec(new_code)
        else: 
            new_line = translator.translate(self.input)
            print(new_line)
            exec(new_line, global_vars, local_vars)
            return global_vars, local_vars
        