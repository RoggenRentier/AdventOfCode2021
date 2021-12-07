import sys
import copy

def reader(file):
    lines = file.read().splitlines()
    return lines


def tooString(arr):
    arrStr = [""] * len(arr)
    for i in range(0, len(arr)):
        arrStr[i] = str(arr[i])
    return ''.join(arrStr)

def getRatingOxGen(arr):
    zero = 0
    one = 0
    pattern = 0    
    for i in range(0, len(arr[0])):
        #Find pattern for this Column (i)
        for j in range(0, len(arr)):
            if arr[j][i] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            pattern = 0
            print("pattern: " + str(pattern))
        else:
            pattern = 1
            print("pattern: " + str(pattern))
        zero = 0
        one = 0

        #throw out values which don't match the pattern
        j = 0
        while j < len(arr):    #iterate
            if str(arr[j][i]) != str(pattern):
                print("pop: " + str(arr[j]))
                arr.pop(j)
                j -= 1          #to avoid skipping
                if len(arr) == 1:
                    return arr[0]
            j += 1
        

def getRatingCo2Scrub(arr):
    zero = 0
    one = 0
    pattern = 0    
    for i in range(0, len(arr[0])):
        #Find pattern for this Column (i)
        for j in range(0, len(arr)):
            if arr[j][i] == "0":
                zero += 1
            else:
                one += 1
        if one >= zero:
            pattern = 0
            print("pattern: " + str(pattern))
        else:
            pattern = 1
            print(str(one) + " not greater " + str(zero))
            print("pattern: " + str(pattern))
        zero = 0
        one = 0

        #throw out values which don't match the pattern
        j = 0
        while j < len(arr):    #iterate
            if str(arr[j][i]) != str(pattern):
                print("pop: " + str(arr[j]))
                arr.pop(j)
                j -= 1          #to avoid skipping
                if len(arr) == 1:
                    return arr[0]
            j += 1
        print(arr)


            


           












file = open("Input/input03.txt")
lines = reader(file)
#lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
#print(lines)

OxGenLines = copy.deepcopy(lines)
Co2Lines = copy.deepcopy(lines)
#print(lines)
#print(Co2Lines)

OxGen = getRatingOxGen(OxGenLines)
decOxGen = int(tooString(OxGen), 2)
print("decOxGen: " + str(decOxGen))
print()

Co2Scrub = getRatingCo2Scrub(Co2Lines)
decCo2Scrub = int(tooString(Co2Scrub), 2)
print("Co2Scrub: " + str(decCo2Scrub))
print()
print(decOxGen * decCo2Scrub)





