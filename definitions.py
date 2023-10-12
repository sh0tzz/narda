
separators = [' ', '\n']

operators = {
    '=':    'OP_SET_VALUE',
    '+':    'OP_ADD',
    '-':    'OP_SUBTRACT',
    '*':    'OP_MULTIPLY',
    '/':    'OP_DIVIDE',
    ';':    'OP_ENDSTATE',
    '(':    'OP_LPAREN',
    ')':    'OP_RPAREN',
    '[':    'OP_LBRACKET',
    ']':    'OP_RBRACKET',
    '{':    'OP_LBRACE',
    '}':    'OP_RBRACE',
    '.':    'OP_DOT',
    ',':    'OP_COMMA',
    '>':    'OP_GREATER',
    '<':    'OP_LESS',
    '!':    'OP_NOT'
}

double_operators = {
    '==':   'OP_EQUAL',
    '>=':   'OP_GEQ',
    '<=':   'OP_LEQ',
    '!=':   'OP_NEQUAL'
}

keywords = {
    'int': 'TYPE_INT',
    'float': 'TYPE_FLOAT',
    'string': 'TYPE_STRING'
}

quotes = {
    "'":    'OP_SINGLEQUOTE',
    '"':    'OP_DOUBLEQUOTE'
}

for key, value in quotes.items():
    operators[key] = value
separators += operators.keys()
