"""
    Make my decision
"""
#   The main of this game is: we make a question to the program and it has to answer

import PySimpleGUI as sg
import random


class MakeMyDecision:
    def __init__(self):
        self.answers = [
            'Yes, of course!',
            'I don\'t know.',
            'Don\'t do that!',
            'I think it\'s the right time.'
        ]
        self.control = True

    def Init(self):
        # Layout
        layout = [
            [sg.Text('Ask me a question:', font=15,
                     justification='center', background_color='green')],
            [sg.Input(size=(100, 5), background_color='blue',
                      text_color='white', font=15)],
            [sg.Output(size=(100, 15), background_color='blue',
                       text_color='white', font=16)],
            [sg.Button('Decide', size=(10, 1)),
             sg.Button('Exit', size=(10, 1))]
        ]
        #   Build the screen
        self.window = sg.Window('Make my decision', size=(
            800, 460), layout=layout, background_color='green')
        while self.control == True:
            #   Read data
            self.event, self.value = self.window.Read()
            #   Do something
            if self.event == 'Decide':
                print(random.choice(self.answers))
            if self.event == 'Exit':
                self.control = False
                self.window.Close()
        # input('Faça sua pergunda: ')


Jogo_1 = MakeMyDecision()
Jogo_1.Init()
