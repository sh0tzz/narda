from os import listdir

def generate_asm(mt, lt, it, et):
    with open('build.cfg', 'r') as f:
        cfg = f.read().split('\n')

    for line in cfg:
        if line.startswith("SOURCE"):
            src = line.split('=')[1]
    with open(f'{src}/template.asm', 'r') as f:
        template = f.read()

    library = ''
    for file in listdir(f'{src}/library'):
        with open(f'{src}/library/{file}', 'r') as f:
            library += "\n\n\n" + f.read()

    code = template.replace('#LIBRARIES#', library)
    # code = template.replace('#LIBRARIES#', '\n')
    return code

