from pathlib import Path

# relative reading
dir_path = Path(__file__).parent
print(dir_path)
file_path = dir_path / 'input.txt'

currentJoltages = 0
totalJoltage = 0
joltageLength = 2
def main():
    global fileHandle
    global currentJoltages
    global totalJoltage
    with file_path.open('r') as fileHandle:
        for currentLine in fileHandle:
            currentJoltages = maxJoltage(currentLine.rstrip())
            print(currentJoltages)
            totalJoltage += int(currentJoltages)
    print(totalJoltage)



def maxJoltage(bank):
    value = []
    for index, currentDigit in enumerate(reversed(bank)):
        #compare the current digit with the value that is in the string
        print("value length:",len(value), "Current Index:", index, "Digit:", currentDigit, "Current Value:", value)
        if (len(value) <= 1 ): #insert items into the list until the length is greater than 2.
            value.insert(0,int(currentDigit)) #insert the current digit to the first spot. 
            continue

        if int(currentDigit) >= int(value[0]): #if the current digit is greater than the left most digit
            #check if value 0 is less than value 1, overwrite value 0
            if int(value[0]) < int(value[1]): #
                value[0]=int(currentDigit)
            else: #if it is greater than or equal, push it in, and pop the back. 
                value.insert(0,int(currentDigit))
                value.pop()


    return ''.join(map(str, value))


main()