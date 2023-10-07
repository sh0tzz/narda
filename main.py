
if __name__ != '__main__':
    raise Exception('main.py cannot be imported')

import lexer as lex

code = '''
int a = 14;
float b => 3.14;
string c <= 'lolcina';
word.strip();
if (name != 'clownface') {
    output("lele mama");
}
'''

parsed_code = lex.parse_code(code)
lexeme_list = lex.start_lexeme_list(parsed_code)
lexeme_list = lex.collapse_operators(lexeme_list)
lex.print(lexeme_list)


# TODO
# lexeme_list = lex.detect_literals(lexeme_list)
# lexeme_list = lex.check_keywords(lexeme_list)

