import PySimpleGUI as sg

class Window:
    def __init__(self):
        sg.theme('DarkPurple5')

        self.passwords = []
        
        layout = [
            [sg.Text('Service:', size=(8,0)), sg.Input(size=(17,0), key='Service')],
            [sg.Text('Password:', size=(8,0)), sg.Input(size=(17,0), key='Password')],
            [sg.Button('Submit')]
        ]

        self.window = sg.Window('Password Rememberer', layout)


    def Init(self):
        while True:
            self.event, self.values = self.window.Read()
            if self.event == sg.WIN_CLOSED:
                break

            self.passwords.append(self.values)
            print(self.passwords[0]["Service"])
            
w = Window()

w.Init()