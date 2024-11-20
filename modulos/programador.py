import pyautogui as pa
import time
import keyboard
import pyperclip

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Programador:

    def Posicionamento(self):   
        #Fixos
        self.centroNota = Ponto(233, 206)
        self.boxAtividade = Ponto(572, 240)
        self.boxAcoes = Ponto(663, 240)
        self.sairPoint = Ponto(117, 55)
        self.cellAcao = Ponto(122, 343) 
        self.cellAcao2 = Ponto(122, 369)
        self.usrealbox = Ponto(281, 343)
        self.termrealbox = Ponto(1109, 343) 
        self.marcarAcao = Ponto(29, 344)
        self.janelaAcoes = Ponto(255, 343)
        self.janelaAcoes2 = Ponto(255, 369)
        self.colarAtividade = Ponto(349, 342)
        
        self.verificador = pa.size()

        if self.verificador[1] == 1080:
            self.medTela = 21

        elif self.verificador[1] == 768:
            self.medTela = 12
    
    def ProgramacaoOrc(self, banconotas, dfOrc):
        pa.PAUSE = 1
        time.sleep(1)
        self.Posicionamento()
        pa.click(self.centroNota.x, self.centroNota.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+a')
        time.sleep(1)
        f = open("LOG.txt", "a")
        f.write("\t*** Log de programação personalizada 0080 ***\n\n")

        for index, row in banconotas.iterrows():
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            if float(row['NOTA']) > 4000000000:
                self.boxAtividade.x = 413
                self.boxAcoes.x = 504
            elif float(row['NOTA']) < 4000000000:
                self.boxAtividade.x = 572
                self.boxAcoes.x = 663
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            fator = 0
            while int(row['NUMMED']) > fator*self.medTela:
                num = fator*self.medTela+1
                if fator > 0:
                    keyboard.press_and_release('pgdown')
                    time.sleep(1)
                fator = fator + 1
            pa.moveTo(29, (306+26.83/2)+(26.83*(int(row['NUMMED'])-num)))
            pa.click()
            pa.click(self.boxAcoes.x, self.boxAcoes.y)
            
            pa.click(self.cellAcao.x, self.cellAcao.y)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y)
            time.sleep(2)
            keyboard.press_and_release('enter')
            time.sleep(2)
            dfOrc.to_clipboard(index = False, header = None)
            pa.click(self.colarAtividade.x, self.colarAtividade.y)
            time.sleep(1)
            keyboard.press_and_release('ctrl+v')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            while True:
                pa.click(self.centroNota.x, self.centroNota.y)
                time.sleep(1)
                keyboard.press_and_release('ctrl+a')
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(2)
                keyboard.press_and_release('ctrl+c')
                time.sleep(1)
                notasalva = pyperclip.paste()
                if notasalva == str(int(row['NOTA'])):
                    pa.click(self.centroNota.x, self.centroNota.y)
                    time.sleep(1)
                    keyboard.press_and_release('ctrl+a')
                    time.sleep(1)
                    self.Posicionamento()
                    f.write(f"Cadastrada: NS {row['NOTA']}, medida: {row['NUMMED']}.\n")
                    break
                time.sleep(10)

    def ProgramacaoGem(self, banconotas, dfGem):
        pa.PAUSE = 1
        time.sleep(1)
        self.Posicionamento()
        pa.click(self.centroNota.x, self.centroNota.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+a')
        time.sleep(1)
        f = open("LOG.txt", "a")
        f.write("   *** Log de programação personalizada Gemini ***\n\n")

        for index, row in banconotas.iterrows():
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            if float(row['NOTA']) > 4000000000:
                self.boxAtividade.x = 413
                self.boxAcoes.x = 504
            elif float(row['NOTA']) < 4000000000:
                self.boxAtividade.x = 572
                self.boxAcoes.x = 663
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            fator = 0
            while int(row['NUMMED']) > fator*self.medTela:
                num = fator*self.medTela+1
                if fator > 0:
                    keyboard.press_and_release('pgdown')
                    time.sleep(1)
                fator = fator + 1
            pa.moveTo(29, (306+26.83/2)+(26.83*(int(row['NUMMED'])-num)))
            pa.click()
            pa.click(self.boxAcoes.x, self.boxAcoes.y)
            
            pa.click(self.cellAcao.x, self.cellAcao.y)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y)
            time.sleep(2)
            keyboard.press_and_release('enter')
            time.sleep(2)
            dfGem.to_clipboard(index = False, header = None)
            pa.click(self.colarAtividade.x, self.colarAtividade.y)
            time.sleep(1)
            keyboard.press_and_release('ctrl+v')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            while True:
                pa.click(self.centroNota.x, self.centroNota.y)
                time.sleep(1)
                keyboard.press_and_release('ctrl+a')
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(2)
                keyboard.press_and_release('ctrl+c')
                time.sleep(1)
                notasalva = pyperclip.paste()
                if notasalva == str(int(row['NOTA'])):
                    pa.click(self.centroNota.x, self.centroNota.y)
                    time.sleep(1)
                    keyboard.press_and_release('ctrl+a')
                    time.sleep(1)
                    self.Posicionamento()
                    f.write(f"Cadastrada: NS {row['NOTA']}, medida: {row['NUMMED']}.\n")
                    break
                time.sleep(10)

    def ProgramacaoAtl(self, banconotas, dfAtl):
        pa.PAUSE = 1
        time.sleep(1)
        self.Posicionamento()
        pa.click(self.centroNota.x, self.centroNota.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+a')
        time.sleep(1)
        f = open("LOG.txt", "a")
        f.write("   *** Log de programação personalizada Atlantis ***\n\n")

        for index, row in banconotas.iterrows():
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            if float(row['NOTA']) > 4000000000:
                self.boxAtividade.x = 413
                self.boxAcoes.x = 504
            elif float(row['NOTA']) < 4000000000:
                self.boxAtividade.x = 572
                self.boxAcoes.x = 663
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            fator = 0
            while int(row['NUMMED']) > fator*self.medTela:
                num = fator*self.medTela+1
                if fator > 0:
                    keyboard.press_and_release('pgdown')
                    time.sleep(1)
                fator = fator + 1
            pa.moveTo(29, (306+26.83/2)+(26.83*(int(row['NUMMED'])-num)))
            pa.click()
            pa.click(self.boxAcoes.x, self.boxAcoes.y)
            
            pa.click(self.cellAcao.x, self.cellAcao.y)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y)
            time.sleep(2)
            keyboard.press_and_release('enter')
            time.sleep(2)
            dfAtl.to_clipboard(index = False, header = None)
            pa.click(self.colarAtividade.x, self.colarAtividade.y)
            time.sleep(1)
            keyboard.press_and_release('ctrl+v')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)
            while True:
                pa.click(self.centroNota.x, self.centroNota.y)
                time.sleep(1)
                keyboard.press_and_release('ctrl+a')
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(2)
                keyboard.press_and_release('ctrl+c')
                time.sleep(1)
                notasalva = pyperclip.paste()
                if notasalva == str(int(row['NOTA'])):
                    pa.click(self.centroNota.x, self.centroNota.y)
                    time.sleep(1)
                    keyboard.press_and_release('ctrl+a')
                    time.sleep(1)
                    self.Posicionamento()
                    f.write(f"Cadastrada: NS {row['NOTA']}, medida: {row['NUMMED']}.\n")
                    break
                time.sleep(12)

    def Programacao75080(self, banconotas, df75080):
        pa.PAUSE = 1
        time.sleep(1)
        self.Posicionamento()
        pa.click(self.centroNota.x, self.centroNota.y)
        time.sleep(1)
        keyboard.press_and_release('ctrl+a')
        time.sleep(1)
        f = open("LOG.txt", "a")
        f.write("   *** Log de programação personalizada 750 - Medida 0080 ***\n\n")

        for index, row in banconotas.iterrows():
            pa.write(str(row['NOTA']), interval=0.1)
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(2.5)
            if float(row['NOTA']) > 4000000000:
                self.boxAtividade.x = 413
                self.boxAcoes.x = 504
            elif float(row['NOTA']) < 4000000000:
                self.boxAtividade.x = 572
                self.boxAcoes.x = 663
            pa.moveTo(self.boxAtividade.x, self.boxAtividade.y)
            pa.click()
            time.sleep(3)
            pa.press('tab')
            fator = 0
            while int(row['NUMMED']) > fator*self.medTela:
                num = fator*self.medTela+1
                if fator > 0:
                    keyboard.press_and_release('pgdown')
                    time.sleep(1)
                fator = fator + 1
            pa.moveTo(29, (306+26.83/2)+(26.83*(int(row['NUMMED'])-num)))
            pa.click()
            pa.click(self.boxAcoes.x, self.boxAcoes.y)
            
            pa.click(self.cellAcao.x, self.cellAcao.y)
            time.sleep(1)
            pa.click(self.janelaAcoes.x, self.janelaAcoes.y)
            time.sleep(3)
            pa.press('down')
            time.sleep(0.5)
            #pa.press('down')
            time.sleep(0.5)
            keyboard.press_and_release('enter')
            time.sleep(1)

            pa.click(self.cellAcao2.x, self.cellAcao2.y)
            time.sleep(1)
            pa.click(self.janelaAcoes2.x, self.janelaAcoes2.y)
            time.sleep(3)
            keyboard.press_and_release('enter')
            time.sleep(1)

            df75080.to_clipboard(index = False, header = None)
            pa.click(self.colarAtividade.x, self.colarAtividade.y)
            time.sleep(1)
            keyboard.press_and_release('ctrl+v')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('enter')
            time.sleep(1)
            keyboard.press_and_release('ctrl+s')
            time.sleep(5)

            while True:
                pa.click(self.centroNota.x, self.centroNota.y)
                time.sleep(1)
                keyboard.press_and_release('ctrl+a')
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(1)
                pyperclip.copy("")
                time.sleep(2)
                keyboard.press_and_release('ctrl+c')
                time.sleep(1)
                notasalva = pyperclip.paste()
                if notasalva == str(int(row['NOTA'])):
                    pa.click(self.centroNota.x, self.centroNota.y)
                    time.sleep(1)
                    keyboard.press_and_release('ctrl+a')
                    time.sleep(1)
                    self.Posicionamento()
                    f.write(f"Cadastrada: NS {row['NOTA']}, medida: {row['NUMMED']}.\n")
                    break
                time.sleep(12)