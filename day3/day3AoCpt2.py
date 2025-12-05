from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'exampleInput.txt'

currentJoltages = 0
totalJoltage = 0
joltageLength = 12 #part 1 is = 2, part 2 = 12
def main():
    global fileHandle
    global currentJoltages
    global totalJoltage
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            currentJoltages = maxJoltage(currentLine.rstrip())
            print(currentLine)
            print(currentJoltages)
            totalJoltage += int(currentJoltages)
    print(totalJoltage)



def maxJoltage(bank):
    value = []
    discardCount = len(bank)-joltageLength #how much can we drop the numbers. 
    print("Bank:", bank)
    for currentDigit in bank:

        while discardCount > 0 and value and currentDigit > value[-1]:
            value.pop()
            discardCount-=1

        value.append(currentDigit)
        
    outputValue = ''.join(map(str, value)) #combine the numbers

    return outputValue[:joltageLength] #trim final count.


main()