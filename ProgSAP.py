import FreeSimpleGUI as sg
import pyautogui as pa
import ctypes
import sys
from modulos import Programador
from modulos import Interface
from PyQt5.QtWidgets import QApplication
from modulos import TableWithExport
import pandas as pd      

verificador = pa.size()
if (verificador[0] != 1920 or verificador[1] != 1080)  or ((ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100) != 1.0):
    sg.popup("A resolução do monitor principal deve ser de 1920x1080p e a escala deve estar em 100%.", button_color="#000000", background_color="#ffffff", text_color="#000000", title="Erro")
    sys.exit()     

janela = Interface()
flagTipo = janela.selecao()

if flagTipo >= 1 and flagTipo <= 7:

    app = QApplication([])
    headers = ['RESP. TEC.', 'MOP', 'CONTRATO', 'COD. CONT.', 'CONTRATADA', 'Ini. Prev.', 'Duração', 'Term. Prev.', 'Term. Real', '%exec', 'Motivo Atraso', 'Observação']
    window = TableWithExport(rows=1, cols=12, headers=headers, arq="df.csv")
    window.show()
    app.exec_()
    df = pd.read_csv("df.csv", sep=',')
    df['COD. CONT.'] = df['COD. CONT.'].apply(lambda x: '{0:0>10}'.format(x))


    app2 = QApplication([])
    headers = ['NOTA', 'NUMMED', 'INIPREV']
    window = TableWithExport(rows=1, cols=3, headers=headers, arq="banconotas.csv")
    window.show()
    app2.exec_()
    banconotas = pd.read_csv("banconotas.csv", sep=',')

    if janela.confirmacaoInicio() == 1:
        janela.aviso()
        programador = Programador("posicionamento.json")

        acoes = []
        match flagTipo:
            case 1:
                acoes = [2]
            case 2:
                acoes = [0, 2]
            case 3:
                acoes = [0, 2]
            case 4:
                acoes = [0, 2]
            case 5:
                acoes = [2]

        programador.programarAtividade(banconotas, df, acoes)

sg.popup('Fim da programação.', button_color="#000000", background_color="#ffffff", text_color="#000000", title="Aviso")