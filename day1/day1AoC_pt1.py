from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

currentIndex = 50 #this is the current dial counter
currentLine = '' #this is the fullstring of the current line
currentCount = 0

def main():
    global fileHandle
    leftOrRight = None
    dialValue = None
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            leftOrRight = currentLine[0]
            dialValue = int(currentLine[1:])
            print('Current Line: ', leftOrRight,dialValue, "Current Index: ", currentIndex)
            updateIndex(leftOrRight, dialValue)
    print('Final is: ', currentCount)    

def updateIndex(firstChar, remainingChars):
    prelimIndex = None
    global currentCount
    global currentIndex
    if firstChar == 'L':
        prelimIndex = currentIndex - remainingChars
    elif firstChar == 'R':
        prelimIndex = currentIndex + remainingChars
    else: 
        print("Ho Ho Hold Up. Something is wrong")

    currentIndex = prelimIndex % 100 #get the remainder to find the correct index
    if currentIndex == 0:
        currentCount += 1


    

main()