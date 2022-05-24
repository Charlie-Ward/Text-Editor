import PySimpleGUI as sg
from pathlib import Path

smileys = [
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
]

smileys_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count', 'Character Count']],
    ['Add', smileys]
]

sg.theme('GrayGrayGray')

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DocName-')],
    [sg.Multiline(no_scrollbar = True, size = (40, 30), key = '-TextBox-')]
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window = True)
        if file_path:
            file = Path(file_path)
            window['-TextBox-'].update(file.read_text())
            window['-DocName-'].update(file_path.split('/')[-1])

    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window = True, save_as = True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TextBox-'])
        window['-DocName-'].update(file_path.split('/')[-1])

    if event == 'Word Count':
        full_text = values['-TextBox-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'Words: {word_count}')

    if event == 'Character Count':
        full_text = values['-TextBox-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'Characters: {char_count}')

    if event in smileys_events:
        full_text = values['-TextBox-']
        new_text = full_text + ' ' + event
        window['-TextBox-'].update(new_text)

window.close()
