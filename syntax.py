import definitions as defs
import language as lang

class Word:
    def __init__(self):
        self.value = ''
    def add(self, token):
        if self.value == '':
            self.value += token
        else:
            self.value += ' ' + token
    def clear(self):
        self.value = ''

def priority_tree(tokens):
    for level in lang.priorities:
        i = 0
        while i < len(tokens):
            if tokens[i] in level:
                if tokens[i-1] == 'VALUE' and tokens[i+1] == 'VALUE':
                    tokens[i] = {
                        'type': 'VALUE',
                        'op':   tokens[i],
                        'op1':  tokens[i-1],
                        'op2':  tokens[i+1]
                    }
                    # TODO
                    del tokens[i-1]
                    del tokens[i+1]
                    i -= 2
            i += 1
    print(tokens)

def check_syntax(tokens):
    word = Word()
    for token in tokens:
        word.add(token)
        if word.value in lang.rules.keys():
            print(lang.rules[word.value])
            word.clear()

