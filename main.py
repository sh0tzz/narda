
if __name__ != '__main__':
    raise Exception('main.py cannot be imported')

from sys import argv
from compiler import compile_code

filename = argv[1]
with open(argv[1], 'r') as f:
    code = f.read()

asm = compile_code(code, True).strip()+'\n'

with open(f'{filename[:filename.rfind(".")]}.asm', 'w') as f:
    f.write(asm)
