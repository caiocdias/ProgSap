import pyautogui as pa
import time
import keyboard
import pyperclip

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Programador:

    def incluirAcoes(self, pos = []):
        offset = 26
        for i, x in enumerate(pos):
            pa.click(self.cellAcao.x, self.cellAcao.y + i * offset)
            time.sleep(1)
            pa.click(self.cellAcao.x, self.cellAcao.y + i * offset)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y + i * offset)
            time.sleep(2)
            for _ in range(x):
                pa.press('down')
                time.sleep(0.2)
            keyboard.press_and_release('enter')

    def colarAtividade(self, df):
        df.to_clipboard(index = False, header = None)
        pa.click(self.BoxColarAtividade.x, self.BoxColarAtividade.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+v')
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('enter')

    def Posicionamento(self):   
        #Fixos
        self.centroNota = Ponto(233, 206)
        self.boxAtividade = Ponto(572, 240)
        self.boxAcoes = Ponto(663, 240)
        self.sairPoint = Ponto(117, 55)
        self.cellAcao = Ponto(122, 343) 
        self.usrealbox = Ponto(281, 343)
        self.termrealbox = Ponto(1109, 343) 
        self.marcarAcao = Ponto(29, 344)
        self.janelaAcoes = Ponto(183, 343)
        self.BoxColarAtividade = Ponto(349, 342)
        self.verificador = pa.size()
        if self.verificador[1] == 1080:
            self.medTela = 21
        elif self.verificador[1] == 768:
            self.medTela = 12
    
    def selecionarNota(self):
        pa.click(self.centroNota.x, self.centroNota.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+a')

    def aguardarSalvamento(self, nota = str):
        while True:
            self.selecionarNota()
            time.sleep(1)
            pyperclip.copy("")
            time.sleep(1)
            pyperclip.copy("")
            time.sleep(2)
            keyboard.press_and_release('ctrl+c')
            time.sleep(1)
            notasalva = pyperclip.paste()
            if notasalva == nota:
                break
            time.sleep(10)

    def verificarManutencao(self, nota = float):
        if nota > 4000000000:
            self.boxAtividade.x = 413
            self.boxAcoes.x = 504
        elif nota < 4000000000:
            self.boxAtividade.x = 572
            self.boxAcoes.x = 663

    def entrarAcaoMedida(self, nummed = int):
        fator = 0
        while nummed > fator*self.medTela:
            num = fator*self.medTela+1
            if fator > 0:
                keyboard.press_and_release('pgdown')
                time.sleep(1)
            fator = fator + 1
        pa.moveTo(29, (306+26.83/2)+(26.83*(nummed-num)))
        pa.click()
        pa.click(self.boxAcoes.x, self.boxAcoes.y)

    def ProgramacaoOrc(self, banconotas, dfOrc):
        pa.PAUSE = 1
        time.sleep(1)

        for index, row in banconotas.iterrows():
            self.Posicionamento
            self.selecionarNota()
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            self.verificarManutencao(float(row['NOTA']))
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            self.entrarAcaoMedida(int(row['NUMMED']))
            time.sleep(2)
            self.incluirAcoes([12])
            time.sleep(2)
            self.colarAtividade(dfOrc)
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            self.aguardarSalvamento(str(int(row['NOTA'])))

    def ProgramacaoGem(self, banconotas, dfGem):
        pa.PAUSE = 1
        time.sleep(1)

        for index, row in banconotas.iterrows():
            self.Posicionamento()
            self.selecionarNota()
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            self.verificarManutencao(float(row['NOTA']))
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            self.entrarAcaoMedida(int(row['NUMMED']))
            time.sleep(2)
            self.incluirAcoes([6, 7, 5, 10])
            time.sleep(2)
            self.colarAtividade(dfGem)
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            self.aguardarSalvamento(str(int(row['NOTA'])))

    def ProgramacaoAtl(self, banconotas, dfAtl):
        pa.PAUSE = 1
        time.sleep(1)

        for index, row in banconotas.iterrows():
            self.Posicionamento()
            self.selecionarNota()
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            self.verificarManutencao(float(row['NOTA']))
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            self.entrarAcaoMedida(int(row['NUMMED']))
            time.sleep(2)
            pa.click(self.cellAcao.x, self.cellAcao.y)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y)
            time.sleep(2)
            keyboard.press_and_release('enter')
            time.sleep(2)
            self.colarAtividade(dfAtl)
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            self.aguardarSalvamento(str(int(row['NOTA'])))

    def Programacao75080(self, banconotas, df75080):
        pa.PAUSE = 1
        time.sleep(1)

        for index, row in banconotas.iterrows():
            self.Posicionamento()
            self.selecionarNota()
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            self.verificarManutencao(float(row['NOTA']))
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            self.entrarAcaoMedida(int(row['NUMMED']))
            self.incluirAcoes([13, 15, 37, 35])
            time.sleep(1)
            self.colarAtividade(df75080)
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            self.aguardarSalvamento(str(int(row['NOTA'])))