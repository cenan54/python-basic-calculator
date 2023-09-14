#thank you for download the program. made by cenan54
#it's a basic calculator program with gui


import tkinter as tk
#importing gui that called tkinter




gui = tk.Tk()


gui.title("Calculator")
window_width, window_height = 438, 550
gui.resizable(False,False)

gui.attributes('-alpha',0.9)

gui.iconbitmap('./assets/math_icon.ico')
gui.configure(background='#1e1f1c')

#for start program center of screen at start
#getting screen resolution
screenWidth=gui.winfo_screenwidth()
screenHeight=gui.winfo_screenheight()
#finds center of screen. we are subtrackting window w/h
#because python gui centered on upper left.
center_x=int(screenWidth/2 - window_width/2)
center_y=int(screenHeight/2 - window_height/2)
#sets the window center of screen
gui.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')




equation_text = ""
equation_label = tk.StringVar()


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text=total

    except SyntaxError:
        equation_label.set("Syntax Error!")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("Not diveded to zero!")
        equation_text = ""

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")


label = tk.Label(gui, text="Hello World!", textvariable=equation_label, font=('Arial', 18), width=31, height=4, bg='#B4B4B3')
label.pack()

frame = tk.Frame(gui)
frame.pack()

button7 = tk.Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7), bg='#EBE4D1')
button7.grid(row=0, column=0)

button8 = tk.Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8), bg='#EBE4D1')
button8.grid(row=0, column=1)

button9 = tk.Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9), bg='#EBE4D1')
button9.grid(row=0, column=2)

button4 = tk.Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4), bg='#EBE4D1')
button4.grid(row=1, column=0)

button5 = tk.Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5), bg='#EBE4D1')
button5.grid(row=1, column=1)

button6 = tk.Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6), bg='#EBE4D1')
button6.grid(row=1, column=2)

button1 = tk.Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1), bg='#EBE4D1')
button1.grid(row=2, column=0)

button2 = tk.Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2), bg='#EBE4D1')
button2.grid(row=2, column=1)

button3 = tk.Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3), bg='#EBE4D1')
button3.grid(row=2, column=2)

button0 = tk.Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0), bg='#EBE4D1')
button0.grid(row=3, column=0)



plus = tk.Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'), bg='#26577C')
plus.grid(row=3, column=2)

minus = tk.Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('+'), bg='#26577C')
minus.grid(row=3, column=1)

multiply = tk.Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'), bg='#26577C')
multiply.grid(row=1, column=3)

divide = tk.Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'), bg='#26577C')
divide.grid(row=0, column=3)

equal = tk.Button(frame, text='=', height=4, width=9, font=35,
                 command=equals, bg='#E55604')
equal.grid(row=3, column=3)

clear = tk.Button(frame, text='C', height=4, width=9, font=35,
                 command=clear, bg='#B4B4B3')
clear.grid(row=2, column=3)


gui.mainloop()
#it keeps program alive unless not iterrupted like
#pressing x or etc.