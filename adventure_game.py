"""
   AdVENTURE GAME
"""
#   The main is to creat different ends based on the given answers

import PySimpleGUI as sg
import random
# Scenario : You are in an war between 2 nations,
# and there are 2 sides: A and B. Only A can win,
# and B will lose! So I have to take right decisions
# in order to win!


class AdventureGame():
    def __init__(self):
        # Norte Lado1, Sul Lado2
        self.question1 = 'Were you born in the north or south? (n/s)'
        # Espada Lado1, Escuto Lado2
        self.question2 = 'Do you prefer sword or shield? (sword/shield)'
        # Linha de frente Lado1, Tatico Lado2
        self.question3 = 'what is your speciality? (front/tactical)'
        self.final1 = 'You are a frontline hero!'
        self.final2 = 'You will be sacrificed in battle!'
        self.final3 = 'You are not able to fight in the battle!'
        self.final4 = 'You will be a hero protecting our troops!'
        self.control = True

    def Init(self):
        #   Build the layout
        layout = [
            [sg.Text('Adventure Game: click on Init to star playing. Write your answer in the line below.', font=15,
                     justification='center', background_color='green')],
            [sg.Output(size=(50, 10), key='output')],
            [sg.Input(size=(50, 0), key='escolha')],
            [sg.Button('Init'), sg.Button('Send Answer'),
             sg.Button('Exit'), sg.Button('Play again')]
        ]
        #   Build the window
        self.window = sg.Window('Adventure Game', layout=layout, size=(
            600, 280), background_color='green')
        while self.control == True:
            # resposta1 = input(self.pergunta1)
            # Read data
            self.ReadValues()
            if self.event == 'Init':
                print(self.question1)
                self.ReadValues()
                if self.values['escolha'] == 'n':
                    # resposta1B = input(self.pergunta2)
                    print(self.question2)
                    self.ReadValues()
                    if self.values['escolha'] == 'sword':
                        self.window.find_element('output').Update('')
                        print(self.final1)
                    if self.values['escolha'] == 'shield':
                        self.window.find_element('output').Update('')
                        print(self.final4)
                if self.values['escolha'] == 's':
                    # resposta1B = input(self.pergunta3)
                    print(self.question3)
                    self.ReadValues()
                    if self.values['escolha'] == 'front':
                        self.window.find_element('output').Update('')
                        print(self.final2)
                    if self.values['escolha'] == 'tactical':
                        self.window.find_element('output').Update('')
                        print(self.final3)
            elif self.event == 'Exit':
                self.control = False
                self.window.Close()
            else:
                self.window.find_element('output').Update('')
                # self.Init()

    def ReadValues(self):
        self.event, self.values = self.window.Read()


Jogo_1 = AdventureGame()
Jogo_1.Init()
