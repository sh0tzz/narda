import definitions as defs
import helpers

class LookupTable:
    def __init__(self, prefix, fields, duplicates=True):
        self.fields = fields.split()
        self.num_fields = len(self.fields)
        self.prefix = prefix
        self.duplicates = duplicates
        self.values = ()
        self.count = 0
        self.last_id = ''

    def add(self, *args):
        assert len(args) == self.num_fields
        if self.duplicates == False:
            for i in range(self.count):
                if args[0] == self.values[i][1]:
                    self.last_id = f'{self.prefix}{i}'
                    return
        self.values += ((
            f'{self.prefix}{self.count}',
            *args
        ),)
        self.count += 1

    def get(self, key, field):
        assert key[0] == self.prefix
        assert field in self.fields
        key = helpers.key_without_prefix(key)
        field = self.fields.index(field)
        return self.values[key][field+1]
    
    def get_last_id(self):
        if self.last_id == '':
            return f'{self.prefix}{self.count-1}'
        temp = self.last_id
        self.last_id = ''
        return temp

    def full(self, literals, identifiers, expressions, spaces=2):
        assert self.prefix == 'M'
        output = ''
        id_len = len(self.get_last_id())
        for i in range(self.count):
            id = self.values[i][0]
            output += id + ' '*(id_len - len(id)+spaces)
            if self.values[i][1] in defs.all_tokens:
                output += self.values[i][1] + '\n'
            else:
                id = self.values[i][1]
                output += id + ' '*(16-len(id))
                output += '-> '
                if id[0] == 'L':
                    output += literals.get(id, 'value') + '\n'
                elif id[0] == 'I':
                    output += identifiers.get(id, 'name') + '\n'
                elif id[0] == 'E':
                    output += expressions.get(id, 'operand1')
                    output += expressions.get(id, 'operation')
                    output += expressions.get(id, 'operand2') + '\n'
                else:
                    raise Exception()
        return output       

    def __str__(self):
        output = ''
        for row in self.values:
            output += f'{row}\n'
        return output


def create_tables(lexeme_list):
    main_table = LookupTable('M', 'token')
    literals = LookupTable('L', 'type value')
    identifiers = LookupTable('I', 'name', duplicates=False)
    expressions = LookupTable('E', 'operation operand1 operand2')
    for i in range(len(lexeme_list)):
        lexeme = lexeme_list[i]
        if lexeme.type in defs.types:
            literals.add(lexeme.type, lexeme.value)
            main_table.add(literals.get_last_id())
        elif lexeme.type == 'IDENTIFIER':
            identifiers.add(lexeme.value)
            main_table.add(identifiers.get_last_id())
        else:
            main_table.add(lexeme.type)
    return main_table, literals, identifiers, expressions
