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

    def Start(self):
        # Criando uma janela
        self.window = sg.Window('Data Simulator', layout=self.layout)
        # Lendo os valores da tela
        self.events, self.values = self.window.Read()
        # Gerando alguma coisa com os valores
        try:
            if self.events == 'yes' or self.events == 'y':
                self.GenerateDataValue()
            elif self.events == 'no' or self.events == 'n':
                print('We appreciate your participation!')
            else:
                print('Please type [yes or no]!')
        except:
                print('There was an error receiving your reply!')

    def GenerateDataValue(self):
        print(random.randint(self.minimum_value, self.maximum_value))

simulator = DataSimulator()
simulator.Start()

    