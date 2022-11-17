import tkinter as tk

class Controler:
    def __init__(self):
        self.model = None
        self.view = None
        self.tela = tk.Tk()

    #composição de view e model
    def inicializa(self, view, model):
        self.view = view
        self.model = model

        #configura os comandos
        self.configura()

    #coamndos
    def configura(self):
        #self.view.botoes_v1['pesquisar_campo']['command'] = lambda: self.processa('teste')
        self.view.botoes_v3['auto_run']['command'] = lambda: self.processa('auto_run')
        self.view.botoes_v1['run']['command'] = lambda: self.processa('RUN')
        self.view.botoes_v3['insere']['command'] = lambda: self.processa('insere')
        self.view.botoes_v3['remove']['command'] = lambda: self.processa('remove')

    #puxa os metodos de model c base nos comandos
    def processa(self, par):
        row_select = self.view.lb_lista.curselection()

        if par == 'remove':
            self.model.remove_instru(row_select[0])
            self.view.v_lista.set(self.model.converte_para_lista())
        elif par == 'insere':
            self.model.atualiza_instru(row_select[0], self.view.entrada_v3['auto_run'].get())
            self.view.v_lista.set(self.model.converte_para_lista())
        elif par == 'auto_run':
            self.model.insere(self.view.entrada_v3['auto_run'].get())
            self.view.v_lista.set(self.model.converte_para_lista())
        elif par == 'RUN':
            self.model.le_lb()

    #atualiza a tela
    @staticmethod
    def executar():
        tk.mainloop()


##################################################################################################################################################################
    #     elif self.model.campo(self.view.radio) and self.model.campo(pesquisa) and par == 'pesquisa':
    #         if self.view.radio == 'titulo':
    #             a = self.model.busca_por_titulo(pesquisa)
    #             self.insere_TV(a)

    #         elif self.view.radio == 'canal':
    #             a = self.model.busca_por_canal(pesquisa)
    #             self.insere_TV(a)

    #         elif self.view.radio == 'categoria':
    #             a = self.model.busca_por_categoria(pesquisa)
    #             self.insere_TV(a)

    # #processador para os raios button
    # def processa_2(self, par):
    #     if par == 'titulo':
    #         self.view.radio = 'titulo'
    #         return self.view.radio
    #     if par == 'canal':
    #         self.view.radio = 'canal'
    #         return self.view.radio
    #     if par == 'categoria':
    #         self.view.radio = 'categoria'
    #         return self.view.radio
