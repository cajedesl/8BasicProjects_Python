"""
Project 2: Kick a number
"""
# The main is generate a random number and each time the user try to guess this number
# the program will verify if it's the number or if it's bigger or lower then the first number

import random
import PySimpleGUI as sg


class KickNumber:
    def __init__(self):
        self.random_value = 0
        self.minimum_value = 1
        self.max_valor = 100
        self.try_again = True
        #   Build Layout
        self.layout = [
            [sg.Text('Kick the number', size=(39, 0), text_color='red')],
            [sg.Input(size=(18, 0), key='KickValue')],
            [sg.Output(size=(39, 10))],
            [sg.Button('Play'), sg.Button('Exit')]
        ]

    def Init(self):
        #   Build the screen
        self.window = sg.Window('Kick a number', layout=self.layout)
        self.GenerateRandomValue()
        # self.PedirValor()
        try:
            while True:
                #   Read the data
                self.event, self.value = self.window.Read()
                #   Do something
                if self.event == 'Play':
                    self.value_kick = self.value['KickValue']
                    while self.try_again == True:
                        if int(self.value_kick) < self.random_value:
                            print('Kick a bigger number! ')
                            # self.PedirValor()
                            break
                        elif int(self.value_kick) > self.random_value:
                            print('Kick a lower number! ')
                            # self.PedirValor()
                            break
                        else:
                            print('Congratulations, you got it right!!!')
                            self.try_again = False
                            break
                if self.event == 'Exit':
                    self.try_again = False
                    self.window.Close()

        except:
            # self.tentar_novamente = False
            # Here I could just call Iniciar() again
            self.Init()
            print('Please type a valid number.')

    # def PedirValor(self):
    #    self.valor_do_chute = input('Chute um valor: ')

    def GenerateRandomValue(self):
        self.random_value  = random.randint(
            self.minimum_value, self.max_valor)


jogo_1 = KickNumber()
jogo_1.Init()
