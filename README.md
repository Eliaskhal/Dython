# Dython: French-to-Python Translator 
## Overview
This Python-to-French Translator project aims to provide a more accessible version of Python for kids, allowing them to code using French keywords. The project consists of two main scripts: `main.py` and `translator.py`. The `main.py` script handles user input or file input, while the translator.py script translates French keywords to Python.
## main.py
### Description
`main.py` serves as the entry point for the Python-to-French Translator. It takes either a command line argument or user input to process Python code written in French.

### Usage
#### To run the translator with a file as input:
```bash
python main.py path/to/your/file.py
```
Or 
```bash
dist/dython.exe path/to/your/file.py
```

#### To run the translator in interactive mode:
```bash
python main.py
```
Or 
```bash
dist/dython.exe
```

### Code Structure
- `global_vars` and `local_vars`: Global and local variable dictionaries used during code execution.
- The script checks if command line arguments are provided; if so, it processes the file. Otherwise, it enters an interactive loop for user input.

## translator.py
### Description
`translator.py` contains the Translator and Parser classes responsible for translating French keywords to Python and parsing input, respectively.

### Keyword Mappings
The `keywords` dictionary maps French keywords to their Python equivalents

<center>

| French      | English   | French      | English   |
|:------------|:----------:|:------------|:---------:|
| importer    | import    | et          | and       |
| de          | from      | ou          | or        |
| comme       | as        | pas         | not       |
| def         | def       | est         | is        |
| classe      | class     | essayer     | try       |
| retour      | return    | sauf        | except    |
| si          | if        | enfin       | finally   |
| sinon       | else      | lever       | raise     |
| sinonsi     | elif      | affirmer    | assert    |
| tantque     | while     | avec        | with      |
| pour        | for       | lambda      | lambda    |
| dans        | in        | imprimer    | print     |
| arret       | break     | entrer      | input     |
| continuer   | continue  | quitter     | exit      |
| passer      | pass      | plage       | range     |
| Vrai        | True      | ouvrir      | open      |
| Faux        | False     | fermer      | close     |
| Aucun       | None      | lire        | read      |
| et          | and       | ecrire      | write     |
| ou          | or        | append      | append    |
| pas         | not       | longeur     | len       |
| est         | is        | chaine      | str       |
| essayer     | try       | flottant    | float     |
| sauf        | except    | liste       | list      |
| enfin       | finally   | tout        | all       |
| lever       | raise     | nimporte    | any       |
| affirmer    | assert    | filtrer     | filter    |
| avec        | with      | somme       | sum       |
| lambda      | lambda    | trier       | sorted    |
| imprimer    | print     | recherche   | search    |
| entrer      | input     | remplacer   | replace   |
| quitter     | exit      | diviser     | split     |

</center>

## Notes
- This project is intended for educational purposes, providing a fun and engaging way for kids to learn programming concepts using their native language.
- Exercise caution when using the translator for non-educational purposes, as the translation might not cover all edge cases or Python features.
