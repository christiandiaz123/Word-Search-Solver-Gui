from tkinter import *
class wordSearchList:
    def __init__(self, root):
        self.wordSearchFrame = Frame(root)
        self.wordSet = set()

        self.wordLabel = Label(self.wordSearchFrame, text="WordSearch List")
        self.wordLabel.grid(row=0, column=0)

        self.myEntry = Entry(self.wordSearchFrame, width=20)
        self.myEntry.grid(row=1, column=0)

        self.confirmWordBtn = Button(self.wordSearchFrame, command=self.addWord, text="Confirm Word")
        self.confirmWordBtn.grid(row=2, column=0,pady=5)

        self.wordSearchFrame.grid(row=0, column=1)
        self.rowCount = 3
    def addWord(self):
        txt = self.myEntry.get()
        Label(self.wordSearchFrame, text=txt).grid(row=self.rowCount, column=0)
        self.rowCount+=1
        self.wordSet.add(txt)
        print(self.wordSet)