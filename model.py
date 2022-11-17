from tkinter.messagebox import showerror, showwarning, showinfo
import pyautogui as pt
import pyperclip as pc
import time

class Model:
    def __init__(self):
        self.instru = []
        self.pausa = 2

    #insere nova instrução a lista
    def insere(self, par):
        self.instru.append(par)

    #remove instroções
    def remove_instru(self, pos):
        self.instru.pop(pos)

    #atualiza instroções
    def atualiza_instru(self, pos, par):
        self.instru.insert(pos, par)

    #retorna a posição na tela desejada
    def tela_pos():
        return pt.position()

    #conveerte para lista
    def converte_para_lista(self):
        s = []
        for f in self.instru:
            s.append(str(f))
        return s
    
    #mostra se a linha está selecionada
    @staticmethod
    def linha_select(select):
        if len(select) != 0:
            return True
        Model.erro('selct')
        return False

    #lê todas as linhas
    def le_lb(self):
        for i in self.instru:
            pars = i.split(':')
            soma = []

            time.sleep(.5)

            for par in pars[1:]:
                soma.append(par)

            self.auto_gui(pars[0], soma)

    #chama metodos do uatogui
    def auto_gui(self, par, par1):
        if par == 'escrever':
            Model.escrever(par1)
        if par == 'click':
            Model.click(par1)
        if par == 'time':
            Model.time_exe(par1)
        if par == 'press':
            Model.pressiona(par1)
        if par == 'copy':
            Model.copiar(par1)
            par2 = ['ctrl', 'v']
            Model.press(par2)

    #pewciona teclas
    @staticmethod
    def pressiona(par):
        if len(par) == 1:
            pt.press(par[0])

        elif len(par) == 2:
            pt.hotkey(par[0], par[1])

        elif len(par) == 3:
            pt.hotkey(par[0], par[1], par[2])

    #clica em determinada area da tela
    def click(par):
        pt.click(x = par[0], y = par[1])

    #escreve
    @staticmethod
    def escrever(par):
        pt.write(par[0])

    #tempo de execução
    @staticmethod
    def time_exe(par = 1):
        pt.PAUSE = par[0]
    
    #copia dados
    @staticmethod
    def copiar(par):
        pc.copy(par[0])

    #verifica se a barra de pesquisa esta preenchina
    def campo(self, t1):
        if t1 != '':
            return True
       
        self.mostra_erro()
        return False
    
    #verifica se um radio button foi selecionado
    def campo(self, par):
        if par != '':
            return True

        self.mostra_erro()
        return False
            
    #mensagem de erro
    def mostra_erro(self, par = 'erro'):
        if par == 'erro':
            showerror('Erro',\
                    'Todo os Campos Devem Ser Preenchidos.')
        if par == 'info':
            showinfo('Resultado',\
                    'Nenhum Video Encontrado na Pesquisa.')
        if par == 'selct':
            showerror('Erro',\
            'Uma linha deve ser selecionada para essa ação!')