def le_lb():
    instrucoes = [
        'escrever:aaaaaaa', 'copy:a copia', 'press:ctrl:t', 'press:ctrl:shift:t', 'press:win', 'time:.5'
    ]
    soma = []
    for i in instrucoes[4:5]:
        pars = i.split(':')

        for par in pars[1:]:
            soma.append(par)
                
        auto_gui(pars[0], soma)

#chama metodos do uatogui
def auto_gui(par, par1):
    if par == 'escrever':
        print(par)
        print(par1[0])
    if par == 'time':
        print(par)
        print(par1)
    if par == 'press':
        print(par)
        if len(par1) == 1:
            print(par1[0])
        if len(par1) == 2:
            print(par1[0] + ' ' + par1[1])
        if len(par1) == 3:
            print(par1[0] + ' ' + par1[1] + ' ' +  par1[2])
    if par == 'copy':
        print(par)
        print(par1[0])
        

if __name__ == '__main__':
    le_lb()