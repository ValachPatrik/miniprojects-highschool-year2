# Patrik Valach
# 8.5.2022

import tkinter
import random

def draw():
    c.delete('all')
    main_var = entr1_var.get()
    size = min((HEIGHT-2*padd)//len(main_var), (WIDTH-2*padd)//19)
    for i in range(len(main_var)):
        w_lenght = random.randrange(2, 11)
        w_poss = random.randrange(w_lenght)
        for j in range(w_lenght):
            shift = j-w_poss
            c.create_rectangle((WIDTH-size)//2+shift*size, padd+i*size,  (WIDTH+size)//2+shift*size, padd+(i+1)*size)    
        c.create_rectangle((WIDTH-size)//2, padd+i*size,  (WIDTH+size)//2, padd+(i+1)*size, outline='red')

WIDTH = 960
HEIGHT = 480
padd = 50

root = tkinter.Tk()
root.title('tajnicka')
root['bg'] = 'light grey'

c = tkinter.Canvas(width=WIDTH, height=HEIGHT, bd=2)
c.grid(row=1, column=0, columnspan=4)


lbl1 = tkinter.Label(root, text='Hladane slovo:', bg='light grey')
lbl1.grid(row=0, column=0, sticky='e', pady=5)

entr1_var = tkinter.StringVar(root, '')
entr1 = tkinter.Entry(root, textvariable=entr1_var)
entr1.grid(row=0, column=1, sticky='w')

btn_draw = tkinter.Button(root, text='Vykresli tajnicku', command=lambda: draw(),width = 13)
btn_draw.grid(row=0, column=2)

btn_end = tkinter.Button(root, text='Exit', command=lambda: root.destroy())
btn_end.grid(row=0, column=3, sticky='e')


c.focus_set()
root.mainloop()