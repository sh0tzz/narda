import config

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

