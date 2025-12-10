from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'exampleInput.txt'

fullField = []
transposeField = []

def main():
    global fileHandle
    global  fullField
    global transposeField
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            splitLine = currentLine.split()
            print(splitLine)
            fullField.append(splitLine)


    transposeField = [list(x) for x in zip(*fullField)]
        

    validateHomework()
#this all needs to be better optimized and 
def validateHomework():
    finalTotal = 0
    outputList = []
    global transposeField
   
    for dataRows in transposeField:
        operation = dataRows[-1]
        dataRows.pop()
        outputList.append( int(eval(operation.join(dataRows))))
    print("Verify:",sum(outputList))
main()

