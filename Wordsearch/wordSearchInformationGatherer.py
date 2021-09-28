from tkinter import *
import time
def confirmBtn():
    SOLIDMAX = 32
    SOLIDMIN = 0
    from wordSearchTable import main as wordSearchMain
    try:
        rowNum = int(rows.get())
        colNum = int(cols.get())
    except:
        Label(root, text=f"Expected an integer, instead got {rows.get()} and {cols.get()}").grid(row=5,column=0, columnspan=2,pady=(10,0))
        return None
    if(not (rowNum<=SOLIDMAX and rowNum>SOLIDMIN and colNum<=SOLIDMAX and colNum>SOLIDMIN)):
        Label(root, text=f"Integer must be between {SOLIDMIN} and {SOLIDMAX}").grid(row=5, column=0,columnspan=2,pady=(10, 0))
        return None
    for widget in root.winfo_children():
        widget.destroy()
    wordSearchMain(root, rowNum, colNum)

root = Tk()

root.title("Word Search Solver")
root.geometry("600x400")#WxH
myLabel1 = Label(root, text="Please input the Number of Rows: ")
myLabel2 = Label(root, text="Please input the Number of Columns: ")
Label(root, text="This is a Word Search Solver").grid(row=0, column=0,columnspan=3, pady=(100,0), padx=(150,0))
Label(root, text="Please put in information about your WordSearch").grid(row=1, column=0, columnspan=3 ,pady=(0,10), padx=(150,0))
rows = Entry(root, width=6, justify='center')
cols = Entry(root, width=6, justify='center')
rows.grid(row=2, column=1)
cols.grid(row=3, column=1)
myLabel1.grid(row=2, column=0, padx=(150,0))
myLabel2.grid(row=3, column=0, padx=(150,0))
btn = Button(root, text="Confirm", command=confirmBtn).grid(row=4, column=0, columnspan=2,pady=(10,0),padx=(180,0))
root.mainloop()