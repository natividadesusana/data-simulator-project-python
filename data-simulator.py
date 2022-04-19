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
        self.finish_message = [
            [sg.Text('We appreciate your participation!')]
        ]
        self.choice_message = [
            [sg.Text('Choose an option [YES/NO]!')]
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
            if self.events == 'yes' or self.events == 'y':
                return self.PlayAgain()
            elif self.events == 'no' or self.events == 'n':
                return self.FinishMessage()
            else:
                return self.ChoiceMessage()
        except:
                return self.ErroMessage()

    def GenerateDataValue(self):
        return random.randint(self.minimum_value, self.maximum_value)

    def PlayAgain(self):
        self.window = sg.Window('Data Simulator', layout=self.layout2)
        self.window.Read()
        try:
            self.layout2
            if self.events == 'Roll the dice again':
                print('ok')
            else:
                return self.FinishMessage()
        except:
            print('There was an error receiving your reply!')

    def FinishMessage(self):
        self.window = sg.Window('Data Simulator', layout=self.finish_message)
        self.window.Read()

    def ChoiceMessage(self):
        self.window = sg.Window('Data Simulator', layout=self.choice_message)
        self.window.Read()

    def ErroMessage(self):
        self.window = sg.Window('Data Simulator', layout=self.erro_message)
        self.window.Read()

simulator = DataSimulator()
simulator.Start()

    