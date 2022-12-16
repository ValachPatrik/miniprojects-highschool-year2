# Patrik Valach
# 03.11.2021

import tkinter
from tkinter import messagebox

def prevod(window, x, y):
    # prevod zo sustavy menšej ako 10 do desiatkovej
    global vysledok
    sucet = 0
    # -------------Check first input-----------------------
    if not x.get().isdigit():
        input1.set('')
        entry1.focus_set()
        return tkinter.messagebox.showerror('First Value Error', 'Input is not possitive or a number')
    else:
        x = int(x.get())
    if x > 10:
        input1.set('')
        entry1.focus_set()
        tkinter.messagebox.showerror('First Value Error', 'Does not support numeral system higher than 10')
        return None
    elif x < 0:
        input1.set('')
        entry1.focus_set()
        tkinter.messagebox.showerror('First Value Error', 'Does not work with negative values')
    #---------------------------------------------------------
    # ---------------- Check second input---------------------
    if not y.get().isdigit():
        input2.set('')
        entry2.focus_set()
        return tkinter.messagebox.showerror('Second Value Error', 'Input is not possitive or a number')
    else:
        y = str(y.get())
    # --------------------------------------------------------
    # -------------------Calculations------------------------
    if x == 10:
        return vysledok.set('Output: {}'.format(sucet))
    else:
        for i in range(len(y)):
            if int(y[i]) >= x:
                input2.set('')
                entry2.focus_set()
                tkinter.messagebox.showerror('Second Value Error', 'Invalid value in given numeral system')
                return None
            sucet += int(y[i])*x**(len(y)-i-1)
    # ------------------------------------------------------
    vysledok.set('Output: {}'.format(sucet))


def end_program():
    # Ask and End program
    global run_loop
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        window.destroy()
        run_loop = False


def output_clear():
    # Empty output field
    vysledok.set('Output:')



# create main window
window = tkinter.Tk()
window.geometry('300x150')
window.title('Premena do desiatkovej sustavy')
window.protocol('WM_DELETE_WINDOW', lambda: end_program())

# set variables
run_loop = True
run_state = tkinter.StringVar(window, 'disabled')
vysledok = tkinter.StringVar(window, 'Output:')

# first input - sustava
label1 = tkinter.Label(window, text='Ciselna sustava').grid(row=0, column=0, pady=8)
input1 = tkinter.StringVar(window)
entry1 = tkinter.Entry(window, textvariable=input1)
entry1.grid(row=0, column=1)

# second input - cislo v sustave
label2 = tkinter.Label(window, text='Cislo v danej sustave').grid(row=1, column=0, pady=8)
input2 = tkinter.StringVar(window)
entry2 = tkinter.Entry(window, textvariable=input2)
entry2.grid(row=1, column=1)

# run button
run1 = tkinter.Button(window, text='Run', command=lambda: prevod(window, input1, input2), state=tkinter.DISABLED)
run1.grid(row=2, column=0, pady=8)

# output
label3 = tkinter.Label(window, textvariable=vysledok).grid(row=2, column=1, pady=8)

# end button
end_btn = tkinter.Button(window, text='End', command=lambda: end_program())
end_btn.grid(row=3, column=0)
end_btn.focus()

# Check change in input
input1.trace('w', lambda a, b, c: output_clear())
input2.trace('w', lambda a, b, c: output_clear())

# main program loop
while run_loop:
    # set run button on/off
    if input1.get() != '' and input2.get() != '':
        run1['state'] = tkinter.NORMAL
        run1['bg'] = 'light green'
    else:
        run1['state'] = tkinter.DISABLED
        run1['bg'] = 'red'
    window.update()
