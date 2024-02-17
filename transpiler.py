from os import listdir

with open('template.asm', 'r') as f:
    template = f.read()

library = ''
for file in listdir('./library'):
    with open(f'./library/{file}', 'r') as f:
        library += "\n\n\n" + f.read()

code = template.replace('#LIBRARIES#', library)
# code = template.replace('#LIBRARIES#', '\n')

def generate_asm(mt, lt, it, et):
    return code

