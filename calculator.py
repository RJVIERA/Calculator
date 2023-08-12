import tkinter as tk 
from tkinter import filedialog,Text
import pstats

calc = ""

def add_calc(symbol):
    global calc 
    calc += str(symbol)
    
    result.delete(1.0,"end")
    result.insert(1.0, calc)
    
def eval_calc():
    global calc
    
    try:
        calc = str(eval(calc))
        result.delete(1.0,"end")
        result.insert(1.0, calc)
    except:
        clear_field()
        result.insert(1.0, "Error")

def clear_field():
    global calc
    calc = ""
    result.delete(1.0,"end")



root = tk.Tk()
root.geometry("300x275")

result = tk.Text(root, height =2, width =16, font =("Calibri", 25))
result.grid(columnspan=5)


#number buttons
bttn_1= tk.Button(root, text="1", command=lambda: add_calc(1), width=5, font=("Calibri", 10))
bttn_1.grid(row=2, column=1)
bttn_2= tk.Button(root, text="2", command=lambda: add_calc(2), width=5, font=("Calibri", 10))
bttn_2.grid(row=2, column=2)
bttn_3= tk.Button(root, text="3", command=lambda: add_calc(3), width=5, font=("Calibri", 10))
bttn_3.grid(row=2, column=3)
bttn_4= tk.Button(root, text="4", command=lambda: add_calc(4), width=5, font=("Calibri", 10))
bttn_4.grid(row=3, column=1)
bttn_5= tk.Button(root, text="5", command=lambda: add_calc(5), width=5, font=("Calibri", 10))
bttn_5.grid(row=3, column=2)
bttn_6= tk.Button(root, text="6", command=lambda: add_calc(6), width=5, font=("Calibri", 10))
bttn_6.grid(row=3, column=3)
bttn_7= tk.Button(root, text="7", command=lambda: add_calc(7), width=5, font=("Calibri", 10))
bttn_7.grid(row=4, column=1)
bttn_8= tk.Button(root, text="8", command=lambda: add_calc(8), width=5, font=("Calibri", 10))
bttn_8.grid(row=4, column=2)
bttn_9= tk.Button(root, text="9", command=lambda: add_calc(9), width=5, font=("Calibri", 10))
bttn_9.grid(row=4, column=3)
bttn_0= tk.Button(root, text="0", command=lambda: add_calc(0), width=5, font=("Calibri", 10))
bttn_0.grid(row=5, column=2)

#operation buttons
bttn_add= tk.Button(root, text="+", command=lambda: add_calc("+"), width=5, font=("Calibri", 10))
bttn_add.grid(row=2, column=4)
bttn_min= tk.Button(root, text="-", command=lambda: add_calc("-"), width=5, font=("Calibri", 10))
bttn_min.grid(row=3, column=4)
bttn_mul= tk.Button(root, text="*", command=lambda: add_calc("*"), width=5, font=("Calibri", 10))
bttn_mul.grid(row=4, column=4)
bttn_div= tk.Button(root, text="/", command=lambda: add_calc("/"), width=5, font=("Calibri", 10))
bttn_div.grid(row=5, column=4)

#parenthesis

bttn_open= tk.Button(root, text="(", command=lambda: add_calc("("), width=5, font=("Calibri", 10))
bttn_open.grid(row=5, column=1)
bttn_close= tk.Button(root, text=")", command=lambda: add_calc(")"), width=5, font=("Calibri", 10))
bttn_close.grid(row=5, column=3)





#additional functions

bttn_clear= tk.Button(root, text="C", command=clear_field, width=10, font=("Calibri", 10))
bttn_clear.grid(row=6, column=1, columnspan=2)
bttn_equals= tk.Button(root, text="=", command=eval_calc, width=10, font=("Calibri", 10))
bttn_equals.grid(row=6, column=3, columnspan=2)




root.mainloop()