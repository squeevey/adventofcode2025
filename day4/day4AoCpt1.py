from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'exampleInput.txt'

warehouseFloor = []

def main():
    global fileHandle
    global warehouseFloor
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            paperLocation = currentLine.rstrip()
            warehouseFloor.append(paperLocation)
    print(warehouseFloor, len(warehouseFloor))
    outputCount = countRolls(warehouseFloor)
    print(outputCount)

def countRolls(floorMap):
    rowMax = len(floorMap)
    copyFloorMap = list()
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
                print("Ranges X & y", xRangeMinus, xRangePlus, yRangeMinus, yRangePlus)
                for x in range(xRangeMinus,xRangePlus+1):
                    for y in range(yRangeMinus,yRangePlus+1):
                        if 0 <= x < colMax and 0 <= y < rowMax and floorMap[y][x]=='@':
                            print("y & x, Char", y, x, floorMap[y][x])
                            tempRoll+=1
                if tempRoll < 4:
                    newRow=newRow+'X'
                    countOfRolls+=1
                else:
                    newRow=newRow+column

                print("Rolls Around:", tempRoll)
        copyFloorMap.append(newRow)
    print(copyFloorMap)
    return countOfRolls


main()