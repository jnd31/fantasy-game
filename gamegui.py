from psg_master import PySimpleGUI as sg


statbar_size = (12,20)
#DarkBrown1
#DarkGreen2
#DarkGreen6
sg.theme('DarkBrown1')


charstats_layout = [[sg.Push(), sg.Text('HP'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-HPbar-')],
                    [sg.Push(), sg.Text('ATK'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-ATKbar-')],
                    [sg.Push(), sg.Text('DEF'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-DEFbar-')],]

map_layout = [[]]

leftside_layout = [[sg.Frame('Character stats', charstats_layout)],
                   [sg.Frame('Map', map_layout)]]

narration_layout = [[sg.Text('Talking talking talking')]]

scene_layout = [[sg.Image(source='images/mouseoutside.gif', zoom=3)],
                [sg.Frame('Narration', narration_layout)]]

button_size = (12, 1)

menu_layout = [[sg.Button('Main Menu', size=button_size)],
               [sg.Button('Save/Load game', size=button_size)],
               [sg.Button('Exit', size=button_size)]] #Exit will be in the main menu but since the menu isnt there yet it's just here for now lol

button_layout = [[sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size), sg.Button('4', size=button_size), sg.Button('5', size=button_size)],
                 [sg.Button('Q', size=button_size), sg.Button('W', size=button_size), sg.Button('E', size=button_size), sg.Button('R', size=button_size), sg.Button('T', size=button_size)],
                 [sg.Button('A', size=button_size), sg.Button('S', size=button_size), sg.Button('D', size=button_size), sg.Button('F', size=button_size), sg.Button('G', size=button_size)]]

layout = [[sg.Column(leftside_layout), sg.Frame('Scene', scene_layout)],
          [sg.Frame('Menu', menu_layout), sg.Frame('Buttons', button_layout)]]

window = sg.Window('Untitled Fantasy Game', layout)



while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-HPbar-'].update(80)

window.close()