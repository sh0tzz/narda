import tkinter as tk
import tkinter.scrolledtext as tkScrolledText
from compiler import compile_code
from json import loads

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x720')
        self.current_tab = None
        self.tabs = {
            'source':    SourceTab(),
            'lexer':     LexerTab(),
            'parser':    ParserTab(),
            'generator': GeneratorTab()
        } 
        NavBar().pack(fill=tk.X)
        self.config = self.import_config('./debugcfg.json')
        self.code = self.load_test_code()
        self.switch_tab('source')
    
    def import_config(self, filename):
        with open(filename, 'r') as f:
            json_config = f.read()
        config = loads(json_config)
        return config
    
    def load_test_code(self):
        if self.config['input_file']:
            with open(self.config['input_file']) as f:
                return f.read()

    def switch_tab(self, tab):
        
        if tab not in self.tabs.keys():
            raise Exception(f'Unknown tab {tab}')
        if self.current_tab != None:
            self.current_tab.pack_forget()
        self.current_tab = self.tabs[tab]
        self.current_tab.pack(fill=tk.BOTH, expand=True)

    def compile(self):
        output = compile_code(self.code)
        self.lexeme_list = output[0]
        self.tables = output[1]
        print(self.lexeme_list, self.tables)



class NavBar(tk.Frame):
    def __init__(self):
        super().__init__()
        tk.Button(self, text='Source code', command=lambda: self.master.switch_tab('source')).pack(side=tk.LEFT)
        tk.Button(self, text='Lexical analysis', command=lambda: self.master.switch_tab('lexer')).pack(side=tk.LEFT)
        tk.Button(self, text='Syntactic analysis', command=lambda: self.master.switch_tab('parser')).pack(side=tk.LEFT)
        tk.Button(self, text='Code Generation', command=lambda: self.master.switch_tab('generator')).pack(side=tk.LEFT)



class SourceTab(tk.Frame):
    def __init__(self):
        super().__init__()
        self.code_box = tkScrolledText.ScrolledText(
            self,
            font=('Courier New', 20, 'bold'),
            width=50
        )
        self.code_box.insert('0.0', self.get_code())
        self.code_box.pack(fill=tk.Y, expand=True)
        tk.Button(self, text='Compile', command=self.compile).pack()

    def get_code(self):
        print(self.master.code)

    def compile(self):
        print(self.master)
        code = self.code_box.get('0.0', tk.END)
        self.master.compile()

class LexerTab(tk.Frame):
    def __init__(self):
        super().__init__()
        tk.Label(self, text='Lexical analysis').pack()

class ParserTab(tk.Frame):
    def __init__(self):
        super().__init__()
        tk.Label(self, text='Syntactic analysis').pack()

class GeneratorTab(tk.Frame):
    def __init__(self):
        super().__init__()
        tk.Label(self, text='Code Generation').pack()


if __name__ == '__main__':
    App().mainloop()
