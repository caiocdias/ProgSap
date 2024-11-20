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
if ((verificador[0] != 1920 or verificador[1] != 1080) and (verificador[0] != 1366 or verificador[1] != 768))  or ((ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100) != 1.0):
    sg.popup("A resolução do monitor principal deve ser de 1920x1080p ou 1366x768p e a escala deve estar em 100%.", icon='logo.ico', button_color="#000000", background_color="#ffffff", text_color="#000000", title="Erro")
    sys.exit()     

janela = Interface()
flagTipo = janela.selecao()

if flagTipo == 1:

    app = QApplication([])
    headers = ['RESP. TEC.', 'MOP', 'CONTRATO', 'COD. CONT.', 'CONTRATADA', 'Ini. Prev.', 'Duração', 'Term. Prev.', 'Term. Real', '%exec', 'Motivo Atraso', 'Observação']
    window = TableWithExport(rows=1, cols=12, headers=headers, arq="dfOrc.csv")
    window.show()
    app.exec_()
    dforc = pd.read_csv("dfOrc.csv", sep=',')
    dforc['COD. CONT.'] = dforc['COD. CONT.'].apply(lambda x: '{0:0>10}'.format(x))


    app2 = QApplication([])
    headers = ['NOTA', 'NUMMED']
    window = TableWithExport(rows=1, cols=2, headers=headers, arq="banconotas.csv")
    window.show()
    app2.exec_()
    banconotas = pd.read_csv("banconotas.csv", sep=',')

    if janela.confirmacaoInicio() == 1:
        janela.aviso()
        programador = Programador()
        programador.ProgramacaoOrc(banconotas, dforc)    

elif flagTipo == 2:
    app = QApplication([])
    headers = ['RESP. TEC.', 'MOP', 'CONTRATO', 'COD. CONT.', 'CONTRATADA', 'Ini. Prev.', 'Duração', 'Term. Prev.', 'Term. Real', '%exec', 'Motivo Atraso', 'Observação']
    window = TableWithExport(rows=1, cols=12, headers=headers, arq="dfGem.csv")
    window.show()
    app.exec_()
    dfGem = pd.read_csv("dfGem.csv", sep=',')
    dfGem['COD. CONT.'] = dfGem['COD. CONT.'].apply(lambda x: '{0:0>10}'.format(x))


    app2 = QApplication([])
    headers = ['NOTA', 'NUMMED']
    window = TableWithExport(rows=1, cols=2, headers=headers, arq="banconotas.csv")
    window.show()
    app2.exec_()
    banconotas = pd.read_csv("banconotas.csv", sep=',')


    if janela.confirmacaoInicio() == 1:
        janela.aviso()
        programador = Programador()
        programador.ProgramacaoGem(banconotas, dfGem) 

elif flagTipo == 3:
    app = QApplication([])
    headers = ['RESP. TEC.', 'MOP', 'CONTRATO', 'COD. CONT.', 'CONTRATADA', 'Ini. Prev.', 'Duração', 'Term. Prev.', 'Term. Real', '%exec', 'Motivo Atraso', 'Observação']
    window = TableWithExport(rows=1, cols=12, headers=headers, arq="dfAtl.csv")
    window.show()
    app.exec_()
    dfAtl = pd.read_csv("dfAtl.csv", sep=',')
    dfAtl['COD. CONT.'] = dfAtl['COD. CONT.'].apply(lambda x: '{0:0>10}'.format(x))


    app2 = QApplication([])
    headers = ['NOTA', 'NUMMED']
    window = TableWithExport(rows=1, cols=2, headers=headers, arq="banconotas.csv")
    window.show()
    app2.exec_()
    banconotas = pd.read_csv("banconotas.csv", sep=',')


    if janela.confirmacaoInicio() == 1:
        janela.aviso()
        programador = Programador()
        programador.ProgramacaoAtl(banconotas, dfAtl) 

elif flagTipo == 4:
    app = QApplication([])
    headers = ['RESP. TEC.', 'MOP', 'CONTRATO', 'COD. CONT.', 'CONTRATADA', 'Ini. Prev.', 'Duração', 'Term. Prev.', 'Term. Real', '%exec', 'Motivo Atraso', 'Observação']
    window = TableWithExport(rows=1, cols=12, headers=headers, arq="df75080.csv")
    window.show()
    app.exec_()
    df75080 = pd.read_csv("df75080.csv", sep=',')
    df75080['COD. CONT.'] = df75080['COD. CONT.'].apply(lambda x: '{0:0>10}'.format(x))


    app2 = QApplication([])
    headers = ['NOTA', 'NUMMED']
    window = TableWithExport(rows=1, cols=2, headers=headers, arq="banconotas.csv")
    window.show()
    app2.exec_()
    banconotas = pd.read_csv("banconotas.csv", sep=',')


    if janela.confirmacaoInicio() == 1:
        janela.aviso()
        programador = Programador()
        programador.Programacao75080(banconotas, df75080)

sg.popup('Fim da programação.', icon='logo.ico', button_color="#000000", background_color="#ffffff", text_color="#000000", title="Aviso")