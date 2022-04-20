# Simulador de dado
# Simulando o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg 

class DataSimulator:
    def __init__(self):
        self.minimum_value = 1
        self.maximum_value = 6
        # Layout
        self.layout = [
            [sg.Text('Roll the dice?')],
            [sg.Button('yes'),sg.Button('no')]
        ]
        self.layout2 = [
            [sg.Text('Your number is:')],
            [sg.Text(self.GenerateDataValue())],
            [sg.Button('Roll the dice again'), sg.Button('Finish')]
        ]
        self.layout3 = [
            [sg.Text('Click to generate a new number!')],
            [sg.Button('play')]
        ]
        self.layout4 = [
            [sg.Text('Your number is:')],
            [sg.Text(self.GenerateDataValue())],
            [sg.Button('Finish')]
        ]
        self.finish_message = [
            [sg.Text('We appreciate your participation!')]
        ]
        self.erro_message = [
            [sg.Text('There was an error receiving your reply!')]
        ]


    def Start(self):
        # Criando uma janela
        self.window = sg.Window('Data Simulator', layout=self.layout)
        # Lendo os valores da tela
        self.events, self.values = self.window.Read()
        # Gerando alguma coisa com os valores
        try:
            if self.events == 'yes':
                return self.PlayAgain()
            else:
                return self.FinishMessage()
        except:
                return self.ErroMessage()

    def GenerateDataValue(self):
        return '🎲', random.randint(self.minimum_value, self.maximum_value)

    def PlayAgain(self):
        self.window = sg.Window('Data Simulator', layout=self.layout2)
        self.events, self.values = self.window.Read()
        try:
            if self.events == 'Roll the dice again':
                return self.ClickPlayAgain()
            else:
                return self.FinishMessage()
        except:
            return self.ErroMessage()

    def ClickPlayAgain(self):
        self.window = sg.Window('Data Simulator', layout=self.layout3)
        self.events, self.values = self.window.Read()
        try:
            if self.events == 'play':
                return self.ReturnPlayAgain()
            else:
                return self.FinishMessage()
        except:
            return self.ErroMessage()

    def ReturnPlayAgain(self):
        self.window = sg.Window('Data Simulator', layout=self.layout4)
        self.events, self.values = self.window.Read()
        try:
            if self.events == 'Finish':
                return self.FinishMessage()
        except:
            return self.ErroMessage()

    def FinishMessage(self):
        self.window = sg.Window('Data Simulator', layout=self.finish_message)
        self.window.Read()

    def ErroMessage(self):
        self.window = sg.Window('Data Simulator', layout=self.erro_message)
        self.window.Read()

simulator = DataSimulator()
simulator.Start()

    