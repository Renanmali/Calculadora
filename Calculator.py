import operation
import tkinter
import customtkinter


window = customtkinter.CTk()
window.title("Calculadora")
window.geometry("800x700")


# window.mainloop()

entry = customtkinter.CTkEntry(window, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('%', 4, 4), ('^', 1, 4), ('√', 2, 4)
]

for (text, row, column) in buttons:
    button = customtkinter.CTkButton(window, text=text, width=100, height=40, font=('Arial', 12),
                                   command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=column)

def on_button_click(text):
    current_text = entry.get()

    if text == 'C':
        entry.delete(0, customtkinter.END)
    elif text == '=':
        try:
            result = evaluate_expression(current_text)
            entry.delete(0, customtkinter.END)
            entry.insert(customtkinter.END, result)
        except Exception as e:
            entry.delete(0, customtkinter.END)
            entry.insert(customtkinter.END, 'Erro')
    else:
        entry.insert(customtkinter.END, text)

def evaluate_expression(expression):
    try:
        expression = expression.replace('x', '*')
        expression = expression.replace('%', '/100')
        expression = expression.replace('^', '**')
        expression = expression.replace('√', '**0.5')
        result = eval(expression, {}, {
            'addition': addition,
            'subtraction': subtraction,
            'division': division,
            'multiplication': multiplication,
            'percent': percent,
            'potentiation': potentiation,
            'radiciation': radiciation
        })
        return result
    except Exception as e:
        raise e

window.mainloop()