import definitions as defs
import helpers

class LookupTable:
    def __init__(self, prefix, fields, duplicates=True):
        self.fields = fields.split()
        self.num_fields = len(self.fields)
        self.prefix = prefix
        self.duplicates = duplicates
        self.values = []
        self.count = 0
        self.last_id = ''
        self.deleted = 0

    def add(self, *args):
        assert len(args) == self.num_fields
        if self.duplicates == False:
            for i in range(self.count - self.deleted):
                if args[0] == self.values[i][1]:
                    self.last_id = f'{self.prefix}{i}'
                    return
        self.values.append((f'{self.prefix}{self.count}', *args))
        self.count += 1

    def remove(self, key):
        key = helpers.key_without_prefix(key, self.deleted)
        del self.values[key]
        self.deleted += 1

    def replace(self, key, *args):
        assert len(args) == self.num_fields
        key_new = helpers.key_without_prefix(key, self.deleted)
        self.values[key_new] = (key, *args)

    def get(self, key, field):
        assert key[0] == self.prefix
        assert field in self.fields
        key = helpers.key_without_prefix(key, self.deleted)
        field = self.fields.index(field)
        return self.values[key][field+1]
    
    def clear_cache(self):
        self.count -= self.deleted
        self.deleted = 0

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
        for i in range(self.count - self.deleted):
            id = self.values[i][0]
            output += id + ' '*(id_len - len(id)+spaces)
            if self.values[i][1] in defs.all_tokens:
                output += self.values[i][1] + '\n'
            else:
                id = self.values[i][1]
                if id == None:
                    output += '\n'
                    continue
                output += id + ' '*(16-len(id))
                output += '-> '
                if id[0] == 'L':
                    output += literals.get(id, 'value') + '\n'
                elif id[0] == 'I':
                    output += identifiers.get(id, 'name') + '\n'
                elif id[0] == 'E':
                    output += expressions.get(id, 'operand1') + " "
                    output += expressions.get(id, 'operation') + " "
                    output += expressions.get(id, 'operand2') + '\n'
                # TODO vrati ovo jebote
                # else:
                #     raise Exception()
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

def collapse_expressions(main_table, literals, identifiers, expressions):
    # # print("---------------")
    # expr_start = None
    # for i in range(main_table.count):
    #     token = main_table.get(f'M{i}', 'token')
    #     # print(token)
    #     if token == 'OP_LPAREN':
    #         expr_start = i
    #         continue
    #     if expr_start != None:
    #         if token == 'OP_RPAREN':
    #             removed = 0
    #             for level in defs.priorities:
    #                 for j in range(expr_start+1, i-removed):
    #                     try:
    #                         token = main_table.get(f'M{j}', 'token')
    #                     except IndexError:
    #                         print(main_table.values)
    #                         print(f'M{j}')
    #                         raise IndexError()
    #                     if token in level:
    #                         prev = main_table.get(f'M{j-1}', 'token')
    #                         next = main_table.get(f'M{j+1}', 'token')
    #                         if not helpers.is_id(prev):
    #                             continue
    #                         if not helpers.is_id(next):
    #                             continue
    #                         expressions.add(token, prev, next)
    #                         main_table.replace(f'M{j-1}', expressions.get_last_id())
    #                         main_table.remove(f'M{j}')
    #                         main_table.remove(f'M{j+1}')
    #                         removed += 2
    #             if main_table.get(f'M{expr_start-1}', 'token')[0] != 'L':
    #                 main_table.remove(f'M{expr_start}')
    #                 main_table.remove(f'M{i-removed}')

    # print("---------------")
    print("[ TODO ]: COLLAPSE EXPRESSIONS")
    return main_table, literals, identifiers, expressions


def detect_fcalls(main_table, literals, identifiers, expressions):
    call_start = None
    call_id = 0
    calls = []
    params = []
    for i in range(main_table.count):
        token = main_table.get(f'M{i}', 'token')
        if token[0] == 'I':
            next = main_table.get(f'M{i+1}', 'token')
            if next == 'OP_LPAREN':
                call_start = i
                continue
        if call_start != None:
            if token == 'OP_RPAREN':
                calls.append((str(call_id), main_table.get(f'M{call_start}', 'token')))
                for j in range(i-1, call_start+1, -1):
                    param = main_table.get(f'M{j}', 'token')
                    if param != 'OP_COMMA':
                        params.append((str(call_id), param))
                main_table.replace(f'M{call_start}', f'F{call_id}')
                for j in range(call_start, i+1):
                    main_table.remove(f'M{j+1}')
                call_start = None
                call_id += 1
    return main_table, calls, params


def detect_variables(main_table, literals, identifiers):
    print('[ DETECT VARIABLES ]')
    main_table.clear_cache()
    variables = []
    for i in range(main_table.count):
        token = main_table.get(f'M{i}', 'token')
        if token == 'NEW_VAR':
            identifier = main_table.get(f'M{i+1}', 'token')
            literal = main_table.get(f'M{i+2}', 'token')
            varname = identifiers.get(identifier, 'name')
            size = literals.get(literal, 'value')
            variables.append((varname, size))
    return variables
