from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

ranges = []
rangeIds = []
readingRanges = True

def main():
    global fileHandle
    global ranges   
    global readingRanges
    global rangeIds
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            strippedLine = currentLine.rstrip()
            if readingRanges:
                if len(strippedLine) == 0:
                    readingRanges = False
                    continue
                else:
                    ranges.append(strippedLine)
            else:
                rangeIds.append(int(strippedLine))

    findFresh()

def findFresh():
    freshCount = 0
    freshList = []
    global ranges
    global rangeIds
    print("Length of ranges",len(ranges), "length of range ids",len(rangeIds))
    for thisRange in ranges:
        thisRangeList = thisRange.split("-")
        for thisId in rangeIds:
            if int(thisRangeList[0]) <= thisId <= int(thisRangeList[1]) and (thisId not in freshList) :
                freshList.append(thisId)
                
    freshCount = len(freshList)
    print("Fresh Count:",freshCount)
main()