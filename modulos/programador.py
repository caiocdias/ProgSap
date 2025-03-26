import pyautogui as pa
import time
import keyboard
import pyperclip
import json

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Programador:
    def __init__(self, json_path):
        self.json_path = json_path

    def incluirAcoes(self, pos=[]):
        if not pos:
            pa.click(self.cellAcao.x, self.cellAcao.y)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y)
            time.sleep(2)
            keyboard.press_and_release('enter')
            return

        offset = 26
        for i, x in enumerate(pos):
            pa.click(self.cellAcao.x, self.cellAcao.y + i * offset)
            time.sleep(1)
            pa.click(self.cellAcao.x, self.cellAcao.y + i * offset)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y + i * offset)
            time.sleep(1)
            for _ in range(x):
                pa.press('down')
                time.sleep(0.2)
            keyboard.press_and_release('enter')


    def colarAtividade(self, df):
        df.to_clipboard(index = False, header = None)
        time.sleep(1)
        pa.click(self.BoxColarAtividade.x, self.BoxColarAtividade.y)
        time.sleep(1)
        pa.click(self.BoxColarAtividade.x, self.BoxColarAtividade.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+v')
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('enter')
    
    def Posicionamento(self):
        with open(self.json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for key, value in data.items():
            setattr(self, key, Ponto(value["x"], value["y"]))

        self.verificador = pa.size()
        self.medTela = 21 if self.verificador[1] == 1080 else 12 if self.verificador[1] == 768 else 0

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

    def programarAtividade(self, banconotas, df, acoes):
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
            self.incluirAcoes(acoes)
            time.sleep(1)
            self.colarAtividade(df)
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            self.aguardarSalvamento(str(int(row['NOTA'])))