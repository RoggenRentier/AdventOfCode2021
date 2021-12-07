def countIncrease(arr):
    numIncrease = 0
    a = arr[0]
    for x in range(1, len(arr)):
        b = arr[x]
        if(a < b):
            print(str(a) + " " + str(b) + " " + str(numIncrease))
            numIncrease += 1
        a = b
    return numIncrease

def reader(file):
    lines = file.readlines()
    number = 0
    for line in lines:
        number += 1
    arr = number * [0]
    i = 0
    for line in lines:
        arr[i] = int(line)
        i += 1
    return arr



file = open("Input\input01.txt", "r")
#inArr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
inArr = reader(file)
print(inArr)
print()
print(countIncrease(inArr))
