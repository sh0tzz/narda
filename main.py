
if __name__ != '__main__':
    raise Exception('main.py cannot be imported')

import symbol_table as st

code = '''
int a = 14;
float b => 3.14;
string c <= 'lolcina';
word.strip();
if (name != 'clownface') {
    output("lele mama");
}
'''

parsed_code = st.parse_code(code)
symbol_table = st.start_symbol_table(parsed_code)
symbol_table = st.collapse_operators(symbol_table)
st.print_symbol_table(symbol_table)


# TODO
# symbol_table = st.detect_literals(symbol_table)
# symbol_table = st.check_keywords(symbol_table)

