
if __name__ != '__main__':
    raise Exception('main.py cannot be imported')

from sys import argv, exit
from compiler import compile_code

filename = argv[1]
with open(argv[1], 'r') as f:
    code = f.read()

output = f'{filename[:filename.rfind(".")]}.asm'
if '-o' in argv:
    output = argv[argv.index('-o')+1]

asm = compile_code(code, True).strip()+'\n'
with open(output, 'w') as f:
    f.write(asm)
