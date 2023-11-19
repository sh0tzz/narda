import definitions as defs

rules = {
    'NEW_VAR IDENTIFIER OP_ENDSTATE':                 'declare_var',
    'NEW_VAR IDENTIFIER OP_SET VALUE OP_ENDSTATE':    'declare_assign_var',
    'IDENTIFIER OP_SET VALUE OP_ENDSTATE':            'assign_var',
}

priorities = [
    ['OP_MULTIPLY', 'OP_DIVIDE'],
    ['OP_ADD', 'OP_SUBTRACT']
]




