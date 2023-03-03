from psg_master import PySimpleGUI as sg
from pynput import keyboard

statbar_size = (12,20)
#DarkBrown1
#DarkGreen2
#DarkGreen6
sg.theme('DarkBrown1')

buying = False
button_size = (12, 1)

menu_layout = [[sg.Button('New Game', s=button_size)],
               [sg.Button('Save/Load game', s=button_size, k='-SL-')],
               [sg.Button('Options', s=button_size, k='-OP-')],
               [sg.Button('Exit', s=button_size)]]

button_iter = ['-1-', '-2-', '-3-', '-4-', '-5-', '-Q-', '-W-', '-E-', '-R-', '-T-', '-A-', '-S-', '-D-', '-F-', '-G-']


charstats_layout = [[sg.Push(), sg.Text('HP'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-HPbar-')],
                    [sg.Push(), sg.Text('ATK'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-ATKbar-')],
                    [sg.Push(), sg.Text('DEF'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-DEFbar-')]]

map_layout = [[]]

leftside_layout = [[sg.Frame('Character stats', charstats_layout)],
                   #[sg.VPush()],
                   [sg.Frame('Map', map_layout)]]

narration_layout = [[sg.Text('Talking talking talking', k='-NAR-')]]

scene_layout = [[sg.Image(source='images/mouseoutside.gif', zoom=3)],
                [sg.Frame('Narration', narration_layout)]]

npcstats_layout = [[sg.Push(), sg.Text('HP'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-NHPbar-')],
                   [sg.Push(), sg.Text('ATK'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-NATKbar-')],
                   [sg.Push(), sg.Text('DEF'), sg.ProgressBar(100, orientation='h', s=statbar_size, key='-NDEFbar-')]]

rightside_layout = [[sg.Frame('NPC stats', npcstats_layout)],
                    [sg.VPush()]]

button_layout = [[sg.Button('1', s=button_size, k='-1-'), sg.Button('2', s=button_size, k='-2-'), sg.Button('3', s=button_size, k='-3-'), sg.Button('4', s=button_size, k='-4-'), sg.Button('5', s=button_size, k='-5-')],
                 [sg.Button('Q', s=button_size, k='-Q-'), sg.Button('W', s=button_size, k='-W-'), sg.Button('E', s=button_size, k='-E-'), sg.Button('R', s=button_size, k='-R-'), sg.Button('T', s=button_size, k='-T-')],
                 [sg.Button('A', s=button_size, k='-A-'), sg.Button('S', s=button_size, k='-S-'), sg.Button('D', s=button_size, k='-D-'), sg.Button('F', s=button_size, k='-F-'), sg.Button('G', s=button_size, k='-G-')]]

game_layout = [[sg.Column(leftside_layout), sg.Frame('Scene', scene_layout), sg.Column(rightside_layout)]]
          #[sg.Frame('Menu', menu_layout), sg.Frame('Buttons', button_layout)]]

saveload_layout = [[]]

history_layout = [[]]

inventory_layout = [[]]

layout = [[sg.TabGroup([[sg.Tab('Main Menu', menu_layout),
                         sg.Tab('Save/Load', saveload_layout),
                         sg.Tab('Game', game_layout),
                         sg.Tab('Inventory', inventory_layout),
                         sg.Tab('History', history_layout)]], enable_events=True, k='-TAB-')],
          [sg.Push(), sg.Frame('Buttons', button_layout), sg.Push()]]

button_text = {'Main Menu': {'-1-': '1', '-2-': '2', '-3-': '3', '-4-': '4', '-5-': '5', '-Q-': 'Q', '-W-': 'W', '-E-': 'E', '-R-': 'R', '-T-': 'T', '-A-': 'A', '-S-': 'S', '-D-': 'D', '-F-': 'F', '-G-': 'G'},
               'Save/Load': {'-1-': '2', '-2-': '2', '-3-': '3', '-4-': '4', '-5-': '5', '-Q-': 'Q', '-W-': 'W', '-E-': 'E', '-R-': 'R', '-T-': 'T', '-A-': 'A', '-S-': 'S', '-D-': 'D', '-F-': 'F', '-G-': 'G'},
                    'Game': {'-1-': '3', '-2-': '2', '-3-': '3', '-4-': '4', '-5-': '5', '-Q-': 'Q', '-W-': 'W', '-E-': 'E', '-R-': 'R', '-T-': 'Wait', '-A-': 'A', '-S-': 'S', '-D-': 'D', '-F-': 'F', '-G-': 'Leave'},
               'Inventory': {'-1-': '2', '-2-': '2', '-3-': '3', '-4-': '4', '-5-': '5', '-Q-': 'Q', '-W-': 'W', '-E-': 'E', '-R-': 'R', '-T-': 'T', '-A-': 'A', '-S-': 'S', '-D-': 'D', '-F-': 'F', '-G-': 'G'},
                 'History': {'-1-': '4', '-2-': '2', '-3-': '3', '-4-': '4', '-5-': '5', '-Q-': 'Q', '-W-': 'W', '-E-': 'E', '-R-': 'R', '-T-': 'T', '-A-': 'A', '-S-': 'S', '-D-': 'D', '-F-': 'F', '-G-': 'G'}}

next_scene = {'-1-': None, '-2-': None, '-3-': None, '-4-': None, '-5-': None, '-Q-': None, '-W-': None, '-E-': None, '-R-': None, '-T-': None, '-A-': None, '-S-': None, '-D-': None, '-F-': None, '-G-': None}

#retrieves the data from the scene and inputs it into a list usable by the program
def find_scene(scene_code):
    pass

#changes all the game elements to go to the scene in the scene code and updates variables necessary to the current scene
def set_scene(window, scene_code):
    scene = find_scene(scene_code)
    window['-NAR-'].update(scene['-NAR-'])
    

#
def update_button_wrt_tab(window, values):
    for k in button_iter:
        n = k[1]
        window[k].update(n+'. '+button_text[values['-TAB-']][k])

def handle_button_press(window, k, values):
    if next_scene[k] != None and values['-TAB-'] == 'Game' and buying == False:
        set_scene(window, next_scene[k])
    print(k+' handled')

window = sg.Window('Untitled Fantasy Game', layout)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    try:
        if key.char in '12345qwertasdfgQWERTASDFG':
            window['-'+key.char.upper()+'-'].click()
    except AttributeError:
        pass

# Collect events until released
#with keyboard.Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()



while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'New Game': #begin character creation
        window['-TAB-'].update('Game') #supposed to change tab to the game tab... it doesnt tho, idk what it does
    elif event in button_iter:
        handle_button_press(window, event, values)
    elif event == '-TAB-':
        update_button_wrt_tab(window, values)
        print(values['-TAB-'])

window.close()
listener.stop()

'''
I'm thinking about the structure of the code, and I think I'll have to have something like... a big list/dict of all the elements for a certain scene
and codes for what scene to go to if a certain button is pressed. Some scenes you get to by dialogue trees and some you get to by moving in the world.
'''