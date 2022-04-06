import PySimpleGUI as sg
from determinante import *

def janela_m2():
    layout = [
            [sg.Text('Matriz 2x2')],
            [sg.Text('Linha 1', size = (7, 0)), sg.Input(size = (8, 0), k = 'l1')],
            [sg.Text('Linha 2', size = (7, 0)), sg.Input(size = (8, 0), k = 'l2')],
            [sg.Text('Det.', size = (7, 0)), sg.Input(k = 'out', size = (8, 0), readonly = True)],
            [sg.Button('Calcular'), sg.Button('Sair')]
            ]
    return sg.Window('2x2', layout, finalize = True)

tela = janela_m2()
while True:
    evento, dados = tela.read()
    if evento in ['Sair', sg.WIN_CLOSED]:
        break
    elif evento == 'Calcular':
        linha1 = [int(x) for x in dados['l1'] if x.isnumeric()]
        linha2 = [int(x) for x in dados['l2'] if x.isnumeric()]
        matriz = [linha1, linha2]
        try:
            tela['out'].update((matriz_2x2(matriz)))
        except:
            sg.popup('Erro')
