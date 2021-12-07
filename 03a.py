def reader(file):
    lines = file.read().splitlines()
    return lines

def getGamma(lines):
    
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

def getEpsilon(gamma):
    epsilon = [0] * len(gamma)
    for i in range(0, len(gamma)):
        if gamma[i] == 0:
            epsilon[i] = 1
        else:
            epsilon[i] = 0

    return epsilon

def tooString(arr):
    arrStr = [""] * len(arr)
    for i in range(0, len(arr)):
        arrStr[i] = str(arr[i])
    return ''.join(arrStr)
        
            








file = open("Input/input03.txt")
lines = reader(file)
#lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
#print(lines)
gamma = getGamma(lines)
epsilon = getEpsilon(gamma)
print(tooString(gamma))
print(tooString(epsilon))

decGamma = int(tooString(gamma), 2)
decEpsilon = int(tooString(epsilon), 2)
print(decGamma)
print(decEpsilon)

print()
print(decGamma * decEpsilon)