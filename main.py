import tkinter as tk

# def window
window = tk.Tk()
window.title('Pizza Order Menu')
window.geometry('1920x720')


def btn(txt):
    btn1 = tk.Button(window, text=txt)
    btn1['width'] = 50
    btn1['height'] = 4
    btn1['activebackground'] = 'red'
    btn1.grid(column=0, row=0)


btn('hihi')

window.mainloop()
