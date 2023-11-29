import tkinter as tk
import tkinter.scrolledtext as tkScrolledText

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
        self.switch_tab('source')

    def switch_tab(self, tab):
        if tab not in self.tabs.keys():
            raise Exception(f'Unknown tab {tab}')
        if self.current_tab != None:
            print('AAAA')
            self.current_tab.pack_forget()
        self.current_tab = self.tabs[tab]
        self.current_tab.pack(fill=tk.BOTH, expand=True)


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
        code_box = tkScrolledText.ScrolledText(self)
        code_box.grid(row=0, column=0, rowspan=2)

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
