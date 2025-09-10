import FreeSimpleGUI as sg
import os

# create history file if not exists
if not os.path.exists("history.txt"):
    with open("history.txt", "w") as file:
        pass

sg.theme("Reddit")

# input field
input_box = sg.InputText(tooltip="Enter Equation", key="equation", focus=True, size=15)

# buttons
buttons = [
    ["9", "8", "7", "+", "x"],
    ["6", "5", "4", "-", "/"],
    ["3", "2", "1", "0", "="]
]

# layout
layout = [[input_box]]
for row in buttons:
    layout.append([sg.Button(b, key=b) for b in row])

layout.append([sg.Button("History", key="history")])

window = sg.Window("Calculator", layout=layout, font=("Helvetica", 16))

current_equation = ""

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event in "0123456789+-/x":
        if event == "x":
            current_equation += "*"
        else:
            current_equation += event
        window["equation"].update(current_equation)

    elif event == "=":
        try:
            result = str(eval(current_equation))
            window["equation"].update(result)

            # save to history
            with open("history.txt", "a") as file:
                file.write(current_equation + " = " + result + "\n")

            current_equation = result
        except Exception:
            window["equation"].update("Error")
            current_equation = ""

    elif event == "history":
        # read history file
        with open("history.txt", "r") as file:
            history_content = file.read() or "No history yet!"
        sg.popup_scrolled(history_content, title="Calculation History", size=(40, 20))

window.close()
