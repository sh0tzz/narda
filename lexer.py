import definitions as defs
import helpers

def parse_code(code):
    def add(token):
        if token.strip() != '':
            parsed_code.append(token)
    parsed_code = []
    word = ''
    for char in code:
        if char in defs.separators:
            add(word.strip())
            add(char)
            word = ''
        else:
            word += char
    add(word.strip())
    return parsed_code

def start_lexeme_list(parsed_code):
    lexeme_list = []
    for symbol in parsed_code:
        if symbol.startswith('_') or helpers.is_char(symbol[0]):
            lexeme_list.append((symbol, 'TEXT'))
        elif helpers.is_digit(symbol[0]):
            lexeme_list.append((symbol, 'NUMBER'))
        elif symbol in defs.separators:
            lexeme_list.append((symbol, 'SEPARATOR'))
        else:
            raise Exception(f'SYMBOL "{symbol}" COULD NOT BE INTERPRETED')
    return lexeme_list

def collapse_operators(lexeme_list):
    for i in range(len(lexeme_list)):
        word = ''
        if lexeme_list[i][1] != 'SEPARATOR':
            word = ''
            continue
        if word + lexeme_list[i][0] in defs.double_operators:
            lexeme_list[i-1] = (word + lexeme_list[i][0], 'SEPARATOR')
            lexeme_list[i] = (None, 'NONE')
            word = ''
        else:
            word = lexeme_list[i][0]
    stripped_table = []
    for item in lexeme_list:
        if item != (None, 'NONE'):
            stripped_table.append(item)
    return stripped_table

def print(lexeme_list):
    for item in lexeme_list:
        print(item)
