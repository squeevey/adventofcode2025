from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

ranges = []


def main():
    global fileHandle
    global ranges   
    global readingRanges
    global rangeIds
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            strippedLine = currentLine.rstrip().split("-")
            if len(strippedLine[0]) == 0:
                break

            ranges.append([int(x) for x in strippedLine])

    findFresh()

def findFresh():
    freshCount = 0
    freshList = []
    global ranges
    sortedRanges = sorted(ranges, key=lambda x: x[0])
    sortedRanges[1]
    for thisRange in sortedRanges:
        
        if len(freshList)==0: #if the freshList is empty just add one in and go to the next loop
            freshList.append(thisRange)
            continue
        freshListLast = freshList[-1] #set the FreshListLast to the Last item
        if (freshListLast[1]< thisRange[0]): #if the next item start range is outside the last item just append it. 
            freshList.append(thisRange)
            continue
        else:
            if(freshListLast[1] >= thisRange[1]): #if the last item's last element is greater or equal to the last item of the next, move on. 
                continue
            if (freshListLast[1] >= thisRange[0] and freshListLast[1]<thisRange[1]): #if the ranges overlap, adjust the last item. 
                freshList.pop()
                freshList.append([freshListLast[0],thisRange[1]])
                continue

    for rangedItem in freshList:
        freshCount += (rangedItem[1]-rangedItem[0])+1 #count the ranges of each. 
    print("Fresh Count:", freshCount)
main()