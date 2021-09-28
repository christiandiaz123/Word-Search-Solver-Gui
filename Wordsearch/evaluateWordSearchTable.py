import re
def leftHorizantal(eGrid, lGrid, yellowGrid, wordSet):
    for erow,lrow,i in zip(eGrid,lGrid, range(len(lGrid))):
        buildStr = ""
        for ele in erow:
            letter = ele.get()
            buildStr += letter
            if(len(letter)!=1):
                raise Exception #TODO Create Exception for this
            lrow.append(letter)
        for word in wordSet:
            pattern = re.compile(word)
            # forward matches
            matches = pattern.finditer(buildStr)
            for match in matches:
                startp, endp = match.span(0)
                while(startp<endp):
                    yellowGrid[i][startp] += 1
                    startp+=1
            # backward matches
            matches = pattern.finditer(buildStr[::-1])
            for match in matches:
                startp, endp = match.span(0)
                endp-=1
                temp = len(buildStr) - endp -1
                endp = len(buildStr) - startp - 1
                startp = temp
                while (startp < (endp+1)):
                    yellowGrid[i][startp] += 1
                    startp += 1
def topVertical(lGrid, yellowGrid, wordSet):
    i = 0
    while (i < len(lGrid[0])):
        ii = 0
        buildStr = ""
        while (ii < len(lGrid)):
            buildStr += lGrid[ii][i]
            ii += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr)
            for match in matches:
                startp, endp = match.span(0)
                while (startp < endp):
                    yellowGrid[startp][i] += 1
                    startp += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr[::-1])
            for match in matches:
                startp, endp = match.span(0)
                endp -= 1
                temp = len(buildStr) - endp - 1
                endp = len(buildStr) - startp - 1
                startp = temp
                while (startp < (endp + 1)):
                    yellowGrid[startp][i] += 1
                    startp += 1

        i += 1
def leftUpwardDiagonal(lGrid, yellowGrid, wordSet):
    i = 0
    while (i < len(lGrid)):
        j = i
        ii = 0
        buildStr = ""
        while (True):
            if (ii >= len(lGrid[0]) or j < 0):
                break
            buildStr += lGrid[j][ii]
            ii += 1
            j -= 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr)
            for match in matches:
                startp, endp = match.span(0)
                while (startp < endp):
                    yellowGrid[i - startp][startp] += 1
                    startp += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr[::-1])
            for match in matches:
                startp, endp = match.span(0)
                endp -= 1
                temp = len(buildStr) - endp - 1
                endp = len(buildStr) - startp - 1
                startp = temp
                while (startp < (endp + 1)):
                    yellowGrid[i - startp][startp] += 1
                    startp += 1
        i += 1
def leftDownwardDiagonal(lGrid, yellowGrid, wordSet):
    i = 0
    while (i < len(lGrid)):
        j = i
        ii = 0
        buildStr = ""
        while (True):
            if (ii >= len(lGrid[0]) or j >= len(lGrid)):
                break
            buildStr += lGrid[j][ii]
            ii += 1
            j += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr)
            for match in matches:
                startp, endp = match.span(0)

                while (startp < endp):
                    yellowGrid[i + startp][startp] += 1
                    startp += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr[::-1])
            for match in matches:
                startp, endp = match.span(0)
                endp -= 1
                temp = len(buildStr) - endp - 1
                endp = len(buildStr) - startp - 1
                startp = temp
                while (startp < (endp + 1)):
                    yellowGrid[i + startp][startp] += 1
                    startp += 1
        i += 1
def bottomRightDiagonal(lGrid, yellowGrid, wordSet):
    i = 1
    while (i < len(lGrid[0])):
        j = i
        ii = len(lGrid) - 1
        buildStr = ""
        while (True):
            if (ii < 0 or j >= len(lGrid[0])):
                break
            buildStr += lGrid[ii][j]
            ii -= 1
            j += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr)
            for match in matches:
                startp, endp = match.span(0)

                while (startp < endp):
                    yellowGrid[-1 - startp][i + startp] += 1
                    startp += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr[::-1])
            for match in matches:
                startp, endp = match.span(0)
                endp -= 1
                temp = len(buildStr) - endp - 1
                endp = len(buildStr) - startp - 1
                startp = temp
                while (startp < (endp + 1)):
                    yellowGrid[-1 - startp][i + startp] += 1
                    startp += 1
        i += 1
def topRightDiagonal(lGrid, yellowGrid, wordSet):
    i = 1
    while (i < len(lGrid[0])):
        j = 0  # Up and Down
        ii = i  # Left and Right
        buildStr = ""
        while (True):
            if (ii >= len(lGrid[0]) or j >= len(lGrid)):
                break
            buildStr += lGrid[j][ii]
            ii += 1
            j += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr)
            for match in matches:
                startp, endp = match.span(0)

                while (startp < endp):
                    yellowGrid[startp][i + startp] += 1
                    startp += 1
        for word in wordSet:
            pattern = re.compile(word)
            matches = pattern.finditer(buildStr[::-1])
            for match in matches:
                startp, endp = match.span(0)
                endp -= 1
                temp = len(buildStr) - endp - 1
                endp = len(buildStr) - startp - 1
                startp = temp
                while (startp < (endp + 1)):
                    yellowGrid[startp][i + startp] += 1
                    startp += 1
        i += 1