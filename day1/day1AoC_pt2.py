from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

currentIndex = 50 #this is the current dial counter
currentLine = '' #this is the fullstring of the current line
currentCount = 0 #this is the count of Zeros
rotaryCount = 100 #this is the amount of numbers on the rotary.

def main():
    global currentIndex
    global fileHandle
    leftOrRight = None
    dialValue = None
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            leftOrRight = currentLine[0]
            dialValue = int(currentLine[1:])
            updateIndex(leftOrRight, dialValue)
    print('Final is: ', currentCount)    

def updateIndex(direction, moveAmount):
    global currentCount
    global currentIndex
    global rotaryCount
    rotaryIndexDiff = None
    print("Current Index:",currentIndex, "Current count: ", currentCount)
    print("Direction:", direction, moveAmount)
    if direction == 'R':
        rotaryIndexDiff = rotaryCount-currentIndex #how much space is left to the end
        if rotaryIndexDiff == moveAmount: #if the increment is the same as the amount set it to zero and move on. 
            currentIndex = 0
            currentCount+=1
        #the following could be optimized better I'm sure.
        elif rotaryIndexDiff < moveAmount: #if the amount of room left is less than movement amount (this can be optimized)
            moveAmount-= rotaryIndexDiff #subtract the amount from the rotarydifference - basically set us to zero and recalculate
            currentCount+=1 #increment the count since we're at 0
            currentCount+= moveAmount//rotaryCount #get the amount we pass zero
            currentIndex = moveAmount%rotaryCount #set the new index
        else:
            currentIndex += moveAmount
    if direction == 'L':

        if currentIndex == moveAmount: #you end up at zero
            currentIndex = 0
            currentCount+=1
        elif currentIndex < moveAmount: #we know we are going to be doing some rollovers
            rotaryIndexDiff=moveAmount-currentIndex #subtract the index from the move amount to set us at 0
            if currentIndex == 0:
                currentCount+=rotaryIndexDiff//rotaryCount
            else:
                currentCount+=1 #add one since we know we know we will rollover. 
                currentCount+=rotaryIndexDiff//rotaryCount
            currentIndex=(-rotaryIndexDiff)%rotaryCount
        else:
            currentIndex-=moveAmount #subtract the amount to get the new index.

main()