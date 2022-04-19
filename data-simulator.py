# Simulador de dado
# Simulando o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI 

class DataSimulator:
    def __init__(self):
        self.minimum_value = 1
        self.maximum_value = 6
        self.message = 'Generate new value for data [Y/N]? '
        # Layout
        layout = [
            [sg.Text('Roll the dice?')],
            [sg.Buttom('Yes'),sg.Button('No')]
        ]
        # Criando uma janela
        window = sg.Window('Data Simulator', Layout=layout)

    def Start(self):
        answer = input(self.message)
        try:
            if answer == 'yes' or answer == 'y':
                self.GenerateDataValue()
            elif answer == 'no' or answer == 'n':
                print('We appreciate your participation!')
            else:
                print('Please type [yes or no]!')
        except:
            print('There was an error receiving your reply!')

    def GenerateDataValue(self):
        print(random.randint(self.minimum_value, self.maximum_value))

simulador = DataSimulator()
simulador.Start()

    