import PySimpleGUI as sg
from Database import DB

class Window:
    def __init__(self, layout_add=False):
        self.layout_add = layout_add

        sg.theme('DarkAmber')
        
        layout_add = [
            [sg.Text('----- ADD PASSWORD -----')],
            [sg.HorizontalSeparator()],
            [sg.Text('Service:', size=(8,0)), sg.Input(size=(20,0), key='Service')],
            [sg.Text('Password:', size=(8,0)), sg.Input(size=(20,0), key='Password')],
            [sg.Button('Add')],
            [sg.Output(size=(25,5))],
        ]

        layout_get = [
            [sg.Text('----- GET PASSWORD -----')],
            [sg.HorizontalSeparator()],
            [sg.Text('Service:', size=(8,0)), sg.Input(size=(20,0), key='ServiceG')],
            [sg.Button('Get')],
            [sg.Output(size=(27,5))],
        ]

        layout = layout_get

        if self.layout_add:
            layout = layout_add

        self.window = sg.Window('Password Rememberer', layout, element_justification='c', size=(250,200))

    def Init(self):
        while True:
            self.event, self.values = self.window.Read()
            if self.event == sg.WIN_CLOSED:
                DB.Die()
                break

            if self.layout_add:
                DB.Create(self.values['Service'], self.values['Password'])

            if not self.layout_add:
                DB.Get(self.values['ServiceG'])
#\/ Add Password \/
#w = Window(True)

#\/ Get Password \/
w = Window()

w.Init()
