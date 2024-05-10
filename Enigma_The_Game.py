import PySimpleGUI as sg
import datetime

class Game:
    sg.change_look_and_feel('SystemDefault1')

    def __init__(self):
        # Layout:
        layout = [
            [sg.Text('Quer Jogar Um Jogo?', font=("AnyFont", 20), justification='center')],
            [sg.Button('Sim', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Enigma The Game', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Sim':
            self.Regras()
    
    def Regras(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('REGRAS:', font=("AnyFont", 18), justification='left')],
            [sg.Text('1° - Não leia o codigo até terminar de resolver.\n2° - Pesquisa é permitida.\n3° - Ajuda é permitida.', font=("AnyFont", 15), justification='left')],
            [sg.Button('Ok', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Enigma The Game', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Ok':
            self.Level1()

    def Level1(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('88886667774442555', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 1', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == "tutorial":
                self.Level2()
            else:
                self.Level1()

    def Level2(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('Que horas são?', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 2', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == str(datetime.datetime.now().hour).zfill(2) + ":" + str(datetime.datetime.now().minute).zfill(2):
                self.Level3()
            else:
                self.Level2()

    def Level3(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('{ +{&{', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 3', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == "o jogo":
                self.Level4()
            else:
                self.Level3()

    def Level4(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('²²Ti', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 4', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == "titânio":
                self.Level5()
            else:
                self.Level4()

    def Level5(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('11101', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 5', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'] == "29":
                self.Level6()
            else:
                self.Level5()
    
    def Level6(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('#CC1100', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 6', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == "blood orange":
                self.Level7()
            else:
                self.Level6()

    def Level7(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('otpnhy', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 7', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == "python":
                self.Level8()
            else:
                self.Level7()

    def Level8(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('Disse-lhe Jesus: "Guarde a espada! Pois todos os que empunham a espada, pela espada morrerão.', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level 8', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() == "mateus 26:52":
                self.Level9()
            else:
                self.Level8()

    def Level9(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('HJXFW', font=("AnyFont", 18), justification='center')],
            [sg.Text('Digite sua resposta:', font=("AnyFont", 15), justification='center')],
            [sg.Input(key='Resposta', font=("AnyFont", 15))],
            [sg.Button('Enviar', font=("AnyFont", 15))]
        ]
        # Janela:
        self.janela = sg.Window('Level x', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()
        if self.event == 'Enviar':
            if self.values['Resposta'].lower() != 'cesar':
                self.Level9()
            else:
                self.Vitoria1()
    
    def Vitoria1(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('Parabens!\nVocê completou todos os enigmas que eu fiz.\nVocê deve ser bem inteligente.', font=("AnyFont", 20), justification='center')],
        ]
        # Janela:
        self.janela = sg.Window('Enigma The Game', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read(timeout=7500)  # Tempo em milissegundos (10 segundos)
        self.Vitoria2()

    
    def Vitoria2(self):
        # Fechar janela anterior:
        self.janela.close()
        # Layout:
        layout = [
            [sg.Text('Esse é meu primeiro Jogo em Python.\nO que achou?', font=("AnyFont", 20), justification='center')],
        ]
        # Janela:
        self.janela = sg.Window('Enigma The Game', layout, element_justification='center')
        # Extrair os dados da tela:
        self.event, self.values = self.janela.read()

Game()