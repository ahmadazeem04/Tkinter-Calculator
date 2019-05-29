##Calculator

import tkinter as tk
from tkinter import messagebox
mainWindow=tk.Tk()#mainWindow is not a keyword
mainWindow.title("Calculator")

heading_label1=tk.Label(mainWindow,text="Enter First Number",pady=(10),padx=(10))
heading_label1.pack()

num_field1=tk.Entry(mainWindow)
num_field1.pack()

heading_label2=tk.Label(mainWindow,text="Enter Second Number",pady=(10),padx=(10))
heading_label2.pack()

num_field2=tk.Entry(mainWindow)
num_field2.pack()

def add():
        var1,var2=valInput()
        result=var1+var2
        #print(result)
        result_label.config(text="Operation result is : "+str(result))

def sub():
        var1, var2 = valInput()
        result = var1 - var2
        result_label.config(text="Operation result is : " + str(result))
        #print(result)

def mul():
        var1, var2 = valInput()
        result = var1 * var2
        #print(result)
        result_label.config(text="Operation result is : " + str(result))

def div():
        var1, var2 = valInput()
        if var2==0:
            result_label.config(text="Operation result is : ")
            messagebox.showerror("Error","Cannot divide the value by zero")
        result = var1 / var2
        #print(result)
        result_label.config(text="Operation result is : " + str(result))


def valInput():
    var1 = num_field1.get()
    var2 = num_field2.get()
    try:
        var1 = int(var1)
        var2 = int(var2)

        return var1,var2
    except ValueError:
        result_label.config(text="Operation result is : ")
        if((len(num_field1.get())==0) or (len(num_field2.get())==0)):
            messagebox.showerror("Error","Please enter a value")
        else:
            messagebox.showerror("Error","Enter only integer value")

heading_label3=tk.Label(mainWindow,text="Operation",pady=(10))
heading_label3.pack()

button1=tk.Button(mainWindow,text="+",command=lambda: add())
button1.pack()

button2=tk.Button(mainWindow,text="-",command=lambda: sub())
button2.pack()

button3=tk.Button(mainWindow,text="*",command=lambda:mul())
button3.pack()

button4=tk.Button(mainWindow,text="/",command=lambda: div())
button4.pack()

result_label=tk.Label(mainWindow)
result_label.pack()

mainWindow.mainloop()