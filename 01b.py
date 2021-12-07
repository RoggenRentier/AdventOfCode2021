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

def threeSum(arr):
    res = [0] * (len(arr) - 2)
    sum = arr[0] + arr[1] + arr[2]
    res[0] = sum

    for i in range(1, len(res)):
       sum = sum - arr[i-1] + arr[i+2]  #equiv sum = arr[i] + arr[i+1] + arr[i+2]
       res[i] = sum 
    
    return res
        



file = open("Input\input01.txt", "r")
#inArr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
inArr = reader(file)
sumArr = threeSum(inArr)
print(sumArr)
print()
print(countIncrease(sumArr))
