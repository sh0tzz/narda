from os import listdir

def load_config():
    with open('build.cfg', 'r') as f:
        cfg = f.read().split('\n')
    config = {}
    for line in cfg:
        if line:
            pair = line.split('=')
            config[pair[0]] = pair[1]
    return config

def load_template(config):
    src = config['SOURCE']
    with open(f'{src}/template.asm', 'r') as f:
        template = f.read()
    return template

def include_libraries(code, config):
    src = config['SOURCE']
    library = ''
    for file in listdir(f'{src}/library'):
        with open(f'{src}/library/{file}', 'r') as f:
            library += "\n\n\n" + f.read()
    return code.replace('#LIBRARIES#', library)

def include_literals(code, literals):
    lits = ''
    for i in range(literals.count - literals.deleted):
        if literals.get(f'L{i}', 'type') == 'STRING':
            value = literals.get(f'L{i}', 'value')
            lits += f'    L{i} db {value}, 0\n'
    return code.replace('#LITERALS#', lits)

def add_function_calls(code, mt, it, lt, calls, params):
    to_add = ""
    mt.clear_cache()
    print('[ ADD FCALLS ]')
    print(calls, params)
    for i in range(mt.count):
        instr = mt.get(f'M{i}', 'token')
        if instr[0] == 'F':
            call_id = int(instr[1:])
            identifier = calls[call_id][1]
            func_name = it.get(identifier, 'name')
            parameters = []
            for tup in params:
                if tup[0] == str(call_id):
                    parameters.append(tup[1])
            if func_name == "print":
                to_add += f"mov rsi, {parameters[0]}\n"
                to_add += "call _puts\n"
            elif func_name == "printline":
                to_add += f"mov rsi, {parameters[0]}\n"
                to_add += "call _puts\n"
                to_add += "call _newl\n"
            elif func_name == "exit":
                value = lt.get(parameters[0], 'value')
                to_add += "mov rax, 60\n"
                to_add += f"mov rdi, {value}\n"
                to_add += "syscall\n"
            elif func_name == "input":
                to_add += "mov rax, 0\n"
                to_add += "mov rdi, 0\n"
                to_add += "mov rsi, INPUT_BUFFER\n"
                to_add += "mov rdx, 64\n"
                to_add += "syscall\n"
    
    return code.replace('#MAIN#', to_add)

def generate_asm(mt, lt, it, et, calls, params):
    config = load_config()
    code = load_template(config)
    code = include_libraries(code, config)
    code = include_literals(code, lt)
    code = add_function_calls(code, mt, it, lt, calls, params)
    return code

