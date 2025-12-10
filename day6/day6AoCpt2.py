from pathlib import Path
import re

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

fullField = []
transposeField = []
splitList = []
widthCounter = []

def main():
    global fileHandle
    global fullField
    global transposeField
    global splitList
    global widthCounter

    pattern = re.compile(r'(\S)(\s+)')

    with file_path.open('r') as fileHandle:
#heres what we should do. Read the last line character by character until we encounter a non-space. 
# count the length. Append that to the width count list. 
# then for all the rows of numbers, we will read in the width, and split the string at that point. Remove the last space.
# then set the remaining spaces == to 0.  These are numerical place hodlers. Then append to the current row,
# repeat until done with the row. append that to the main list. Then validate. 

        for currentLine in fileHandle:
            fullField.append(currentLine)
    #process the operations into the op and its spaces.
    matches = pattern.findall(fullField[-1])
    fullField.pop()

    # put the white space count in the widthCounter, and put the oeprations in the results. 
    results = []
    for char, whitespaceStr in matches:
        widthCounter.append(len(whitespaceStr))
        results.append(char)
    #this last increment captures the lack of space on the last column
    widthCounter[-1]=widthCounter[-1]+1
    # now for each row we're goign to trim off the width of the string.
    for row in fullField:
        splitRow = []
        start = 0
        for width in widthCounter:
            splitRow.append(str(row[start:(start + width)]))
            start += width+1
        splitList.append(splitRow)
    #now transpose the field.
    transposeField = [list(x) for x in zip(*splitList)]

    finalField=[]
    #in this loop we're combining the strings to create the correct number and appending the operator [ numstring1, ..., numstringX, operator]
    for index, tRow in enumerate(transposeField):
        listBuild = list(map(''.join, zip(*tRow)))
        listBuild.append(results[index])
        finalField.append(listBuild)

    print(finalField)
    validateHomework(finalField)
'''

    #splitList.append(results)
    #
'''
def validateHomework(preppedField):
    finalTotal = 0
    outputList = []
    global finale

    for dataRows in preppedField:
        operation = dataRows[-1] #get the operation we're going to perform
        dataRows.pop() #remove the operation.
        #join the strings with the operator, and then evaluate them as ints
        outputList.append( int(eval(operation.join(dataRows))))
    print("Verify:",sum(outputList))
main()