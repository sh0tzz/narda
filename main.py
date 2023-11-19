
if __name__ != '__main__':
    raise Exception('main.py cannot be imported')

import lexer as lex
import syntax as syn

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

parsed_code = lex.parse_code(code)
lexeme_list = lex.start_lexeme_list(parsed_code)
lexeme_list = lex.collapse_operators(lexeme_list)
lexeme_list = lex.detect_literals(lexeme_list)
lexeme_list = lex.detect_keywords(lexeme_list)
lexeme_list = lex.assign_token_abstractions(lexeme_list)
lex.final_check(lexeme_list)
# lex.printlex(lexeme_list)

mt, lt, it, et = syn.create_tables(lexeme_list)
# TODO zagrade i druge operacije
mt, lt, it, et = syn.collapse_expressions(mt, lt, it, et)
print(mt.full(lt, it, et))
print()
print(lt)
print()
print(et)
print()
print(it)

