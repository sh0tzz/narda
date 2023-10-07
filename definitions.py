
separators = [' ', '\n']

operators = {
    '=':    'OP_SET_VALUE',
    '+':    'OP_ADD',
    '-':    'OP_SUBTRACT',
    '*':    'OP_MULTIPLY',
    '/':    'OP_DIVIDE',
    ';':    'OP_EXECUTE',
    '(':    'OP_LPAREN',
    ')':    'OP_RPAREN',
    '[':    'OP_LBRACKET',
    ']':    'OP_RBRACKET',
    '{':    'OP_LBRACE',
    '}':    'OP_RBRACE',
    '.':    'OP_DOT',
    ',':    'OP_COMMA',
    "'":    'OP_SINGLEQUOTE',
    '"':    'OP_DOUBLEQUOTE',
    '>':    'OP_GREATER',
    '<':    'OP_LESS',
    '!':    'OP_NOT'
}

double_operators = {
    '==':   'OP_EQUALS',
    '>=':   'OP_GE',
    '<=':   'OP_LE',
    '!=':   'OP_NOTEQUAL'
}

keywords = {
    'int': 'TYPE_INT',
    'float': 'TYPE_FLOAT',
}


separators += operators.keys()
