# ABSTRACTIONS MUST NOT START WITH 'L', 'I' OR 'E'

separators = [' ', '\n']

operators = {
    '=':    'OP_SET',
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
    'let':      'NEW_VAR',
    'if':       'STATE_IF',
    'else if':  'STATE_ELSEIF',
    'else':     'STATE_ELSE',
    'for':      'STATE_FOR',
    'while':    'STATE_WHILE'
}

quotes = {
    "'":    'OP_SINGLEQUOTE',
    '"':    'OP_DOUBLEQUOTE'
}

types = ['INT', 'FLOAT', 'BOOL', 'STRING']
bool_literals = {
    "true": "BOOL_TRUE",
    "false": "BOOL_FALSE"
}

priorities = [
    ['OP_MULTIPLY', 'OP_DIVIDE'],
    ['OP_ADD', 'OP_SUBTRACT']
]

all_tokens = ['IDENTIFIER']
all_tokens += types
all_tokens += operators.values()
all_tokens += double_operators.values()
all_tokens += keywords.values()
all_tokens += quotes.values()

for key, value in quotes.items():
    operators[key] = value
separators += operators.keys()
