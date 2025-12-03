from pathlib import Path
import re #import regular expression library

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

currentIndex = 50 #this is the current dial counter
currentLine = '' #this is the fullstring of the current line
currentCount = 0
inputList = None
rollingSum = 0
def main():
    global rollingSum
    '''#This was the Part one filter
    regexPattern = re.compile(r'^(\d+)\1$') #Part One
    '''
    regexPattern = re.compile(r'^(\d+)\1+$') #This is the Part Two Filter.
    global fileHandle
    inputList = None
    with file_path.open('r') as fileHandle:
        for line in fileHandle.readlines():
            inputList = line.rstrip().split(',')
    
    for valueRange in inputList:
        valueSetSplit = valueRange.split('-')
        for value in range(int(valueSetSplit[0]),int(valueSetSplit[1])+1):
            valueStr = str(value)
            if regexPattern.search(valueStr):
                rollingSum+=int(valueStr)
                #print(valueStr)
    print('Final Sum: ',rollingSum)
    
main()