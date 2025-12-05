from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

warehouseFloor = list()

def main():
    global fileHandle
    global warehouseFloor
    outputDiff = True
    outputCount=0
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            paperLocation = currentLine.rstrip()
            warehouseFloor.append(paperLocation)
    print(warehouseFloor, len(warehouseFloor))
    while outputDiff:
        tempOutput = countRolls(warehouseFloor)
        print("TempOut: ",tempOutput)
        if tempOutput == 0:
            outputDiff = False
        outputCount+=tempOutput
          
    print(outputCount)

def countRolls(floorMap):
    global warehouseFloor
    rowMax = len(floorMap)
    copyFloorMap = []
    tempRoll = 0
    countOfRolls = 0
    for rowIndex, row in enumerate(floorMap):
        colMax = len(row)
        newRow = ''
        yRangeMinus = rowIndex-1
        yRangePlus = rowIndex+1       
        for columnIndex, column in enumerate(row):
            xRangeMinus = columnIndex-1
            xRangePlus = columnIndex+1
            if column != '@':
                newRow=newRow+column
                continue
            else:
                tempRoll = -1 #subtract this since we'll count our self farther down. 
                #print("Ranges X & y", xRangeMinus, xRangePlus, yRangeMinus, yRangePlus)
                for x in range(xRangeMinus,xRangePlus+1):
                    for y in range(yRangeMinus,yRangePlus+1):
                        if 0 <= x < colMax and 0 <= y < rowMax and floorMap[y][x]=='@':
                            tempRoll+=1
                if tempRoll < 4:
                    newRow=newRow+'.'
                    countOfRolls+=1
                else:
                    newRow=newRow+column
        copyFloorMap.append(newRow)
    warehouseFloor.clear()
    warehouseFloor = copyFloorMap.copy()
    print(warehouseFloor)
    print(countOfRolls)
    return countOfRolls


main()