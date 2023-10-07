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

def start_symbol_table(parsed_code):
    symbol_table = []
    for symbol in parsed_code:
        if symbol.startswith('_') or helpers.is_char(symbol[0]):
            symbol_table.append((symbol, 'TEXT'))
        elif helpers.is_digit(symbol[0]):
            symbol_table.append((symbol, 'NUMBER'))
        elif symbol in defs.separators:
            symbol_table.append((symbol, 'SEPARATOR'))
        else:
            raise Exception(f'SYMBOL "{symbol}" COULD NOT BE INTERPRETED')
    return symbol_table

def collapse_operators(symbol_table):
    for i in range(len(symbol_table)):
        if symbol_table[i][1] != 'SEPARATOR':
            word = ''
            continue
        if word + symbol_table[i][0] in defs.double_operators:
            print(f'FOUND {word + symbol_table[i][0]}')
            symbol_table[i-1] = (word + symbol_table[i][0], 'SEPARATOR')
            symbol_table[i] = (None, 'NONE')
            word = ''
        else:
            word = symbol_table[i][0]
    stripped_table = []
    for item in symbol_table:
        if item != (None, 'NONE'):
            stripped_table.append(item)
    return stripped_table

def print_symbol_table(symbol_table):
    for item in symbol_table:
        print(item)
