import definitions as defs
import helpers

def parse_code(code):
    def add(token):
        if token.strip() != '':
            parsed_code.append(token)
    word = ''
    parsed_code = []
    in_string = False
    quote_type = None
    # "lele! mama"
    for i in range(len(code)):
        char = code[i]
        added = False
        if not in_string:
            if char in defs.quotes:
                in_string = True
                quote_type = char
            if char in defs.separators and char not in defs.quotes:
                add(word.strip())
                add(char)
                word = ''
            else:
                word += char
        elif in_string:
            if char == quote_type:
                quote_type = None
                in_string = False
            word += char
            added = True
    add(word.strip())
    return parsed_code

class Lexeme:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def __str__(self):
        return f'{self.type}\t {self.value}'

def start_lexeme_list(parsed_code):
    lexeme_list = []
    for symbol in parsed_code:
        if symbol.startswith('_') or helpers.is_char(symbol[0]):
            lexeme_list.append(Lexeme(symbol, 'TEXT'))
        elif helpers.is_digit(symbol[0]):
            lexeme_list.append(Lexeme(symbol, 'NUMBER'))
        elif symbol in defs.separators:
            lexeme_list.append(Lexeme(symbol, 'SEP'))
        elif helpers.is_string(symbol):
            lexeme_list.append(Lexeme(symbol, 'STRING'))
        else:
            raise Exception(f'SYMBOL "{symbol}" COULD NOT BE INTERPRETED')
    return lexeme_list

def collapse_operators(lexeme_list):
    word = ''
    for i in range(len(lexeme_list)):
        lexeme = lexeme_list[i]
        if lexeme.type != 'SEP':
            word = ''
            continue
        if word + lexeme.value in defs.double_operators:
            lexeme_list[i-1] = Lexeme(word + lexeme.value, 'SEP')
            lexeme_list[i] = Lexeme(None, None)
            word = ''
        else:
            word = lexeme.value
    return helpers.clean_lexemes(lexeme_list)

def detect_literals(lexeme_list):
    in_number = False
    in_float = False
    for i in range(len(lexeme_list)):
        lexeme = lexeme_list[i]
        if not in_number:
            if lexeme.type == 'NUMBER':
                in_number = True
            continue
        if in_number:
            if lexeme.type == 'SEP':
                if lexeme.value == '.':
                    in_float = True
                    continue
                else:
                    lexeme_list[i-1].type = 'INT'
                    in_number = False
                    in_float = False
                    continue
        if in_float:
            if lexeme.type == 'NUMBER':
                new_lexeme = ''
                new_lexeme += lexeme_list[i-2].value 
                new_lexeme += lexeme_list[i-1].value
                new_lexeme += lexeme_list[i].value
                lexeme_list[i-2] = Lexeme(new_lexeme, 'FLOAT')
                lexeme_list[i-1] = Lexeme(None, None)
                lexeme_list[i] = Lexeme(None, None)
            in_number = False
            in_float = False
    return helpers.clean_lexemes(lexeme_list)

def detect_keywords(lexeme_list):
    for lexeme in lexeme_list:
        if lexeme.value in defs.keywords:
            lexeme.type = 'KEYWORD'
    return lexeme_list

def printlex(lexeme_list):
    for item in lexeme_list:
        print(item)
