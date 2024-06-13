from logging.config import valid_ident

import PySimpleGUI as sg

# define the layout
layout = [
    [sg.Text("Enter a number")],
    [sg.Input(key="-INPUT-")],
    [sg.Button("Square"), sg.Button("Cube"), sg.Button("Exit")],
]
# creat a window
window = sg.Window("Window Operation", layout)

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Square":
        num = float(values["-INPUT-"])
        result = num ** 2
        sg.popup(f"The queare of numbers {num} is : {result}")
    elif event == "Cube":
        num = float(values["-INPUT-"])
        result = num ** 3
        sg.popup(f"The cude of numbers {num} is: {result}")

# window close
window.close()