import config
import definitions as defs

def is_char(symbol):
    assert len(symbol) == 1
    upper_chars = range(ord('A'), ord('Z')+1)
    lower_chars = range(ord('a'), ord('z')+1)
    ascii = ord(symbol)
    if ascii in upper_chars or ascii in lower_chars:
        return True
    return False

def is_digit(symbol):
    assert len(symbol) == 1
    digits = range(ord('0'), ord('9')+1)
    ascii = ord(symbol)
    if ascii in digits:
        return True
    return False

def is_number(symbol):
    for char in str(symbol):
        if not is_digit(char):
            return False
    return True

def is_string(word):
    if word[0] in defs.quotes:
        if word[-1] in defs.quotes:
            return True
    return False

def clean_lexemes(lexemes):
    new_lexemes = []
    for lexeme in lexemes:
        if lexeme.type != None:
            new_lexemes.append(lexeme)
    return new_lexemes

if config.test_code:
    assert is_char('@') == False
    assert is_char('A') == True
    assert is_char('Z') == True
    assert is_char('[') == False
    assert is_char('`') == False
    assert is_char('a') == True
    assert is_char('z') == True
    assert is_char('{') == False

if config.test_code:
    assert is_digit('/') == False
    assert is_digit('0') == True
    assert is_digit('9') == True
    assert is_digit(':') == False

def key_without_prefix(key, deleted):
    if key == None:
        return None
    new_key = ''
    for i in range(1, len(key)):
        new_key += key[i]
    return int(new_key) - deleted

def is_id(id, keys=['L', 'I', 'E']):
    if is_number(id[1:]):
        if id[0] in keys:
            return True
    return False
