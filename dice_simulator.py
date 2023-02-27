"""
Project 1: Dice Simulator
"""
# The main is just to use PySimpleGUI and random library in order to generate
# an interactive simple game

import random
import PySimpleGUI as sg


class DiceSimulator:
    def __init__(self):
        self.minimum_value = 1
        self.maximum_value = 6
        # self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
        # Build a layout
        self.layout = [
            [sg.Text('Play the dice?')],
            [sg.Button('Yes'), sg.Button('No')]
        ]

    def Begin(self):
        # Build a screen
        self.window = sg.Window('Dice Simulator', layout=self.layout)
        # Read values on the screen
        self.event, self.values = self.window.Read()
        # Do something with these values
        # resposta = input(self.mensagem)
        try:
            if self.event == 'Yes' or self.event == 'y':
                self.GenerateDiceValue()
            elif self.event == 'No' or self.event == 'n':
                print('Thank you for your participation.')
            else:
                print('Please click Yes or No.')
        except:
            print('Something went wrong in your answer.')


    def GenerateDiceValue(self):
        print(random.randint(self.minimum_value, self.maximum_value))


simulador_1 = DiceSimulator()
simulador_1.Begin()
