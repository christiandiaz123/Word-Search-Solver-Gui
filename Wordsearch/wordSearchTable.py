from tkinter import *

HEXCOLORS = {
        1:"#FF0000",
        2:"#800000",
        3:"#008000",
        4:"#808000",
        5:"#000080",
        6:"#800080",
        7:"#008080",
        8:"#008080",
        9:"#808080"
    }
def main(root, rows, cols):
    import wordSearchListClass
    currentHeight = 250
    currentWidth = 250
    myFrame = Frame(root)
    entryGrid = []
    letterGrid = []
    for i in range(cols):
        Label(myFrame, text=f"{i + 1}").grid(row=0, column=i+1, padx=2, pady=2)
        currentWidth+=25
    for i in range(rows):
        currentHeight += 25
        entryGrid.append([])
        letterGrid.append([])
        Label(myFrame, text=f"{i+1}").grid(row=i+1, column=0, padx=2, pady=2)
        for ii in range(cols):
            e = Entry(myFrame, width=3, justify='center')
            e.grid(row=i+1, column=ii+1, padx=2, pady =2)
            entryGrid[i].append(e)
    myFrame.grid(row=0,column=0,padx=100,pady=(100,5))
    wordList = wordSearchListClass.wordSearchList(root)
    currentWidth += 175
    confirmBtn = Button(root, text="Confirm Word Search", command=lambda : confirmWordSearch(entryGrid, letterGrid, myFrame, wordList.wordSet)).grid(row=rows+1, column=0)
    currentHeight += 25
    root.geometry(f"{currentWidth}x{currentHeight}")
    #confirmWordSearch(entryGrid, letterGrid)

def confirmWordSearch(eGrid, lGrid, frame, wordSet=set()):
    import evaluateWordSearchTable
    yellowGrid = [[0 for i in range(len(erow))] for erow in eGrid]
    evaluateWordSearchTable.leftHorizantal(eGrid, lGrid, yellowGrid, wordSet)
    evaluateWordSearchTable.topVertical(lGrid, yellowGrid, wordSet)
    evaluateWordSearchTable.leftUpwardDiagonal(lGrid, yellowGrid, wordSet)
    evaluateWordSearchTable.bottomRightDiagonal(lGrid, yellowGrid, wordSet)
    evaluateWordSearchTable.leftDownwardDiagonal(lGrid, yellowGrid, wordSet)
    evaluateWordSearchTable.topRightDiagonal(lGrid, yellowGrid, wordSet)
    for ele in frame.winfo_children():
        if(type(ele)==type(Entry())):
            letter = ele.get()
            eleInfo = ele.grid_info()
            ele.destroy()
            if(yellowGrid[eleInfo["row"]-1][eleInfo["column"]-1]):
                label = Label(frame, text=letter, width=2, bg = HEXCOLORS[yellowGrid[eleInfo["row"]-1][eleInfo["column"]-1]])
            else:
                label = Label(frame, text=letter, width=2)
            label.grid(row=eleInfo["row"], column=eleInfo["column"], padx = 2, pady =2)



