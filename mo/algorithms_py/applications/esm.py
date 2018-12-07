import tkinter as tk
import sys
def F(X):
    return round(-0.04 * X ** 3 + X ** 2 + X -1, 4)

def esm_min(H, X0, max_k=7):
    k = 0
    YF0 = F(X0)
    X1 = round(X0 + H, 4) 
    YF1 = F(X1)

    while k < max_k:
        k += 1
        print(f"1) k = {k}\n")
        print(f"2) y(k) >= y(k-1) -> {YF1} >= {YF0}\n")

        if YF1 >= YF0:
            print("\tTrue\n")
            X1 = X0
            YF1 = YF0
        else:
            print("\tFalse\n")
            print(f"\tx(k+1) = {X1} + {H} = {round(X1 + H, 4)}\n")
            X0 = X1
            YF0 = YF1
            X1 = round(X1 + H, 4)
            YF1 = F(X1)
            print(f"3) y(k+1) = f(x(k+1)) = {YF1}\n")
            print(f"4) k < k_max -> {k} < {max_k}")
            print(f"\t{k < max_k}\n\n\n")
    print(f'x = {X1}\n')
    print(f'y = {YF1}')


class ESM(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widget()

    def create_complex(self, label, l_column, l_row, entry_width, entry_column, entry_row):
        label = tk.Label(self.master, text=label)
        label.grid(column=l_column, row=l_row)
        entry = tk.Entry(self.master, width=entry_width)
        entry.grid(column=entry_column, row=entry_row)
        return label, entry

    def create_widget(self):
        f_title, self.f_entry = self.create_complex('f=', 0, 0, 10, 1, 0)
        h_title, self.h_entry = self.create_complex('H=', 0, 1, 2, 1, 1)
        x0_title, self.x0_entry = self.create_complex('x0=', 0, 2, 2, 1, 2)
        k_max_title, self.k_max_entry = self.create_complex('k_max=', 0, 3, 2, 1, 3)
        file_title, self.file_entry = self.create_complex('file=', 0, 4, 10, 1, 4)
        evaluate_btn = tk.Button(self.master, text='evaluate', command=self.evaluate)\
            .grid(column=0, row=5)
        
        
    def evaluate(self):
        sys.stdout = open(self.file_entry.get(), "w+")
        esm_min(float(self.h_entry.get()),
                int(self.x0_entry.get()))

        


root = tk.Tk()
root.geometry('500x300')
root.title("ESM")
app = ESM(root)

app.mainloop()