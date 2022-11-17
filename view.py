import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

class V1:
    def __init__(self, tela):
        self.tela = tela
        self.botoes_v1 = {}
        self.entrada_v1 = {}

        self.f0 = tk.Frame(self.tela, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f0.pack(side = tk.TOP, fill = tk.BOTH)

        self.botoes_v1['run'] = tk.Button(self.f0, text = 'RUN', bg = 'red', fg = 'white')
        self.botoes_v1['run'].pack(fill = tk.BOTH)

class V2:
    def __init__(self, tela):
        self.tela = tela
        self.botoes_v2 = {}
        self.entrada_v2 = {}

        self.f1 = tk.Frame(self.tela, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f1.pack(side = tk.TOP, fill = tk.BOTH)

        self.entrada_v2['press_keys'] = tk.Entry(self.f1)
        self.entrada_v2['press_keys'].pack(side = tk.LEFT, fill = tk.Y, ipadx = 150)


class V3:
    def __init__(self, tela):
        self.tela = tela
        self.botoes_v3 = {}
        self.entrada_v3 = {}
        self.v_lista = tk.StringVar()

        self.f2 = tk.Frame(self.tela, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f2.pack(side = tk.TOP, fill = tk.BOTH)

        self.f22 = tk.Frame(self.f2, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f22.pack(side = tk.BOTTOM, fill = tk.BOTH)

        self.f20 = tk.Frame(self.f2, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f20.pack(side = tk.LEFT, fill = tk.BOTH)

        self.f21 = tk.Frame(self.f2, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f21.pack(side = tk.LEFT, fill = tk.BOTH)

        

        self.entrada_v3['auto_run'] = tk.Entry(self.f20)
        self.entrada_v3['auto_run'].pack(fill = tk.BOTH, ipadx = 150)


        self.botoes_v3['auto_run'] = tk.Button(self.f21, text = 'auto_run', bg = 'red', fg = 'white')
        self.botoes_v3['auto_run'].pack(side = tk.LEFT, fill = tk.BOTH)
        self.botoes_v3['remove'] = tk.Button(self.f21, text = 'remove', bg = 'red', fg = 'white')
        self.botoes_v3['remove'].pack(fill = tk.BOTH, side = tk.LEFT)
        self.botoes_v3['insere'] = tk.Button(self.f21, text = 'insere', bg = 'red', fg = 'white')
        self.botoes_v3['insere'].pack(fill = tk.BOTH, side = tk.LEFT)

        #listbox
        self.lb_lista = tk.Listbox(self.f22, listvariable = self.v_lista, width = 100)
        

        sb_y_autoRun = ttk.Scrollbar(self.f22, orient = tk.VERTICAL, command = self.lb_lista.yview)
        self.lb_lista.configure(yscroll = sb_y_autoRun.set)

        sb_x_autoRun = ttk.Scrollbar(self.f22, orient = tk.HORIZONTAL, command = self.lb_lista.xview)
        self.lb_lista.configure(xscroll = sb_x_autoRun.set)
        
        sb_x_autoRun.pack(fill = tk.X, side = tk.BOTTOM)
        self.lb_lista.pack(fill = tk.BOTH, side = tk.LEFT)
        sb_y_autoRun.pack(fill = tk.Y, side = tk.LEFT)
        
class V4:
    def __init__(self, tela):
        self.tela = tela
        self.botoes_v4 = {}
        self.entrada_v4 = {}
        self.videos_pesquisa = tk.StringVar(value = f'pos: {0}x, {0}y')

        self.f3 = tk.Frame(self.tela, bd = 10, bg = 'white', relief = tk.RAISED)
        self.f3.pack(side = tk.RIGHT, fill = tk.BOTH)

        self.botoes_v4['pesquisar_pos'] = tk.Button(self.f3, text = 'pesquisar_pos', bg = 'red', fg = 'white')
        self.botoes_v4['pesquisar_pos'].pack( fill = tk.BOTH)

class View(V1, V2, V3):
    def __init__(self, tela, title):
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial", size=12, weight=font.BOLD) 
        V3.__init__(self, tela)
        V1.__init__(self, tela)
        V2.__init__(self, tela)
        self.tela.title(title)

    def __str__(self):
        return 'View\n'

#labelframe c os radius buttons
# lf1 = tk.LabelFrame(f2, text = 'Quero Pesquisar:')
# lf1.grid(row = 3 , column = 0)

#radios buttons
# self.radios['titulo'] = tk.Radiobutton(lf1, text = 'Titulo', value = 'titulo')
# self.radios['titulo'].grid(row = 0, column = 0)
# self.radios['canal'] = tk.Radiobutton(lf1, text = 'Canal.', value = 'canal')
# self.radios['canal'].grid(row = 0, column = 1)
# self.radios['categoria'] = tk.Radiobutton(lf1, text = 'Categoria', value = 'categoria')
# self.radios['categoria'].grid(row = 0, column = 2)