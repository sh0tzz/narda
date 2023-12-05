import lexer as lex
import syntax as syn

def compile_code(code, debug=False):
    parsed_code = lex.parse_code(code)
    lexeme_list = lex.start_lexeme_list(parsed_code)
    lexeme_list = lex.collapse_operators(lexeme_list)
    lexeme_list = lex.detect_literals(lexeme_list)
    lexeme_list = lex.detect_keywords(lexeme_list)
    lexeme_list = lex.assign_token_abstractions(lexeme_list)
    lex.final_check(lexeme_list)
    mt, lt, it, et = syn.create_tables(lexeme_list)
    # TODO zagrade i druge operacije
    mt, lt, it, et = syn.collapse_expressions(mt, lt, it, et)
    if debug:
        lex.printlex(lexeme_list)
        print(mt.full(lt, it, et))
        print()
        print(lt)
        print()
        print(et)
        print()
        print(it)
    return lexeme_list, (mt, lt, it, et)
