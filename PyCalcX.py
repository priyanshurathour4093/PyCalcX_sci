from tkinter import *
import math

first_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def delete():
    current = result_label['text']
    result_label.config(text=current[:-1])

def get_operator(op):
    global first_number, operator
    first_number = float(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number, operator
    try:
        second_number = float(result_label['text'])
        if operator == '+':
            result_label.config(text=str(first_number + second_number))
        elif operator == '-':
            result_label.config(text=str(first_number - second_number))
        elif operator == '*':
            result_label.config(text=str(first_number * second_number))
        elif operator == '/':
            if second_number == 0:
                raise ZeroDivisionError
            result_label.config(text=str(round(first_number / second_number, 2)))
        elif operator == '%':
            result_label.config(text=str(first_number % second_number))
    except (ZeroDivisionError, ValueError):
        result_label.config(text='Error')

def calculate_function(func):
    try:
        num = float(result_label['text'])
        if func == 'log':
            if num <= 0:
                raise ValueError
            result_label.config(text=str(round(math.log10(num), 5)))
        elif func == 'sqrt':
            if num < 0:
                raise ValueError
            result_label.config(text=str(round(math.sqrt(num), 5)))
        elif func == 'sin':
            result_label.config(text=str(round(math.sin(math.radians(num)), 5)))
        elif func == 'cos':
            result_label.config(text=str(round(math.cos(math.radians(num)), 5)))
        elif func == 'tan':
            if (num % 90 == 0) and (num % 180 != 0):
                raise ValueError
            result_label.config(text=str(round(math.tan(math.radians(num)), 5)))
        elif func == 'square':
            result_label.config(text=str(num ** 2))
    except ValueError:
        result_label.config(text='Error')

root = Tk()
root.title('Scientific Calculator')
root.geometry('280x500')
root.resizable(0, 0)
root.configure(background='black')

result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=4, pady=(50, 25), sticky='w')
result_label.config(font=('verdana', 24, 'bold'))

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('log', 5, 0), ('sqrt', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
    ('tan', 6, 0), ('%', 6, 1), ('square', 6, 2), ('Del', 6, 3)
]

for (text, row, col) in buttons:
    if text in {'+', '-', '*', '/', '%'}:
        cmd = lambda x=text: get_operator(x)
    elif text in {'log', 'sqrt', 'sin', 'cos', 'tan', 'square'}:
        cmd = lambda x=text: calculate_function(x)
    elif text == '=':
        cmd = get_result
    elif text == 'C':
        cmd = clear
    elif text == 'Del':
        cmd = delete
    else:
        cmd = lambda x=text: get_digit(x)
    
    btn = Button(root, text=text, bg='#00a65a', fg='white', width=5, height=2, command=cmd)
    btn.grid(row=row, column=col)
    btn.config(font=('verdana', 14))

root.mainloop()