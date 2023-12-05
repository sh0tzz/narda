
if __name__ != '__main__':
    raise Exception('main.py cannot be imported')

from compiler import compile_code

code = '''
let a = 14 / 7;
let b = 3.14 * 2;
let c = 'lolcina';
let d = 1 - 2 + 3 / 4;
c = 5;
word.strip();
let x = 1.0;
if (name != 'clownface') {
    output("lele! m'ama");
} else if (name == false != true)
'''

compile_code(code, True)
