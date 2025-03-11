import FreeSimpleGUI as sg


class Interface:  
    def confirmacaoInicio(self):
        layout = [[sg.Button('Iniciar Programação', key='ok'), sg.Button('Sair', key='cancel')]]
        
        self.win = sg.Window('Confirmação de Inicio', layout = layout, button_color=("#ffffff", "#000000"),
                                background_color="#ffffff", sbar_background_color="#ffffff",
                                sbar_arrow_color="#000000", text_justification='center', resizable=True)
        while True:
            event, values = self.win.read()
            if event == 'ok':
                self.win.close()
                return 1
            elif event == sg.WIN_CLOSED or event == 'cancel':
                self.win.close()
                return 0
    
    def selecao(self):
        menudef = [["Ajuda", ["Abrir", "Contato"]]]
        layout = [
            [sg.Menu(menu_definition=menudef, background_color="#ffffff", text_color="#000000")],
            [sg.Button('Atualizar Gemini', key='kgem', font=("Arial", "11")),
             sg.Button('Atualizar Atlantis', key='katl', font=("Arial", "11")),
             sg.Button('0070', key='k0070', font=("Arial", "11")),
             sg.Button('0750 - Medida 0070', key='k75080', font=("Arial", "11")),
             sg.Button('0170', key='k0170', font=("Arial", "11")),
             sg.Button('0750 - Medida 0170 - 4 ações', key='k7501704', font=("Arial", "11")),
             sg.Button('0750 - Medida 0170 - 7 ações', key='k7501707', font=("Arial", "11")),
             sg.Button('Sair', font=("Arial", "11"))]
            ]
        self.win = sg.Window('Interface de Seleção', layout = layout,
                              background_color="#ffffff", button_color=("#ffffff", "#000000"))
        while True:
            event, values = self.win.read()
            if event == "Abrir":
                layouhelp = [
                    [sg.Text('Escolha a modalidade de programação.', text_color="#000000", background_color="#ffffff")],
                    [sg.Text('Mantenha a resolução e a escala do monitor de acordo com a opção selecionada.', text_color="#000000", background_color="#ffffff")], 
                    [sg.Text('Preencha devidamente as janelas.', text_color="#000000", background_color="#ffffff")], 
                    [sg.Text('Mantenha o SAP ao fundo, maximizado e na transação iw52.', text_color="#000000", background_color="#ffffff")], 
                    [sg.Text('Mantenha o layout da janela ações no layout global.', text_color="#000000", background_color="#ffffff")],
                    [sg.Text('Instabilidades nos sistemas Cemig podem implicar em erros na execução da programação.', text_color="#000000", background_color="#ffffff")],
                    [sg.Button('Ok')]]
                
                sg.Window(layout=layouhelp, title="Ajuda",button_color="#000000", background_color="#ffffff").read(close=True)
            elif event == "Contato":
                sg.popup('Para suporte contate: Caio Cezar Dias', button_color='#000000', text_color='#000000', background_color="#ffffff")
                
            elif event == 'k0070':
                self.win.close()
                return 1
            elif event == 'kgem':
                self.win.close()
                return 2
            elif event == 'katl':
                self.win.close()
                return 3
            elif event == 'k75080':
                self.win.close()
                return 4
            elif event == 'k0170':
                self.win.close()
                return 5
            elif event == 'k7501704':
                self.win.close()
                return 6
            elif event == 'k7501707':
                self.win.close()
                return 7
            elif  event == sg.WIN_CLOSED or event == 'Sair':
                self.win.close()
                break

    def aviso(self):
        sg.popup('Certifique-se que o SAP está aberto na transação IW52 e está em destaque no monitor principal. O programa trabalhará com automatização de mouse e teclado, evite utilizar estas vias na máquina que está executando o programa, a não ser que deseje parar sua execução.',
                 button_color='#000000', text_color='#000000', background_color="#ffffff")