import lexer as lex
import syntax as syn
import transpiler as tpl

def compile_code(code, debug=False):
    parsed_code = lex.parse_code(code)
    lexeme_list = lex.start_lexeme_list(parsed_code)
    lexeme_list = lex.collapse_operators(lexeme_list)
    lexeme_list = lex.detect_literals(lexeme_list)
    lexeme_list = lex.detect_keywords(lexeme_list)
    lexeme_list = lex.assign_token_abstractions(lexeme_list)
    lex.final_check(lexeme_list)
    mt, lt, it, et = syn.create_tables(lexeme_list)
    
    if debug:
        lex.printlex(lexeme_list, end='\n')
        print(mt.full(lt, it, et), end='\n')
        print(mt, end='\n')
        print(lt, end='\n')
        print(et, end='\n')
        print(it, end='\n')
    
    mt, lt, it, et = syn.collapse_expressions(mt, lt, it, et)
    for i in range(mt.count):
        key = f'M{i}'
        value = mt.get(key, 'token')
        print(f'{key}\t{value}')
    
    mt, calls, params = syn.detect_fcalls(mt, lt, it, et)
    asm = tpl.generate_asm(mt, lt, it, et, calls, params)
    for i in calls:
        print(i)
    print()
    for i in range(len(params)):
        if i != 0:
            if last != params[i][0]:
                print()
        print(params[i])
        last = params[i][0]
    return asm
