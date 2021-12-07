import sys

def reader(file):
    lines = file.read().splitlines()
    return lines

def getOxGenPattern(lines):
    
    zero = 0
    one = 0
    arr = [0] * len(lines[0])
    
    for i in range(0, len(lines[0])):
        for line in lines:
            if line[i] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:   
            arr[i] = 0
        else:
            arr[i] = 1
        zero = 0
        one = 0

    return arr

def getCo2ScrubPattern(gamma):
    epsilon = [0] * len(gamma)
    for i in range(0, len(gamma)):
        if gamma[i] == 0:
            epsilon[i] = 1
        else:
            epsilon[i] = 0

    return epsilon

def deepFuckingCopy(arr):
    copyArr = [[0] * len(arr[0])] * len[arr] 
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            copyArr[i][j] = arr[i][j]

def tooString(arr):
    arrStr = [""] * len(arr)
    for i in range(0, len(arr)):
        arrStr[i] = str(arr[i])
    return ''.join(arrStr)

def getRating(pattern, arr):
    for j in range(0, len(pattern)):
        i = 0
        while i < len(arr):
            if arr[i][j] != pattern[j]:
                arr.pop(i)
                print("arrlen: " + str(len(arr)))
                i -= 1 
            if len(arr) == 1:
                print("feddisch")
                return arr[0]
                
            i +=1
           


        
            








#file = open("Input/input03.txt")
#lines = reader(file)
lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
#print(lines)

OxGenLines = deepFuckingCopy(lines)
Co2Lines = deepFuckingCopy(lines)
print(lines)
print(Co2Lines)

OxGenPat = getOxGenPattern(lines)
Co2ScrubPat = getCo2ScrubPattern(OxGenPat)
print(tooString(OxGenPat))
print(tooString(Co2ScrubPat))
'''OxGen = getRating(OxGenPat, lines)
print("first Rating fin")
Co2Scrub = getRating(Co2ScrubPat, lines)
decOxGen = int(tooString(OxGen), 2)
decEpsilon = int(tooString(Co2Scrub), 2)
print(decOxGen)
print(decEpsilon)
print()
print(decOxGen * decEpsilon)
'''




