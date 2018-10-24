import tkinter as tk
import random
COLS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ROWS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

window = tk.Tk()
window.geometry('500x300')

window.title("Welcome to Tkinter")

clicked_cnt = 0

label = tk.Label(window, text='i am a label', font=("Arial Bold", 25))
label.grid(column=0, row=0)

btn = None

def make_plus_one():
	global clicked_cnt, btn
	label.configure(text='clicked {} times'.format(clicked_cnt))
	clicked_cnt += 1
	x	
	btn.grid(column=random.choice(range(0, 100)), row=random.choice(range(0, 100)))

btn = tk.Button(window, text='+1', command=make_plus_one)

btn.grid(column=1, row=0)







window.mainloop()