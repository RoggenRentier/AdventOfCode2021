import time

startTime = time.time()

def reader(file):
    fish = file.readline().split(",")
    for i in range(0, len(fish)):
        fish[i] = int(fish[i])
    return fish

def eval(fish):
    count = [0,0,0,0,0,0,0,0,0]
    for e in fish:
        count[e] += 1

    print("initial count: " + str(count))
    print()
    return count





file = open("Input/input06.txt")
fish = reader(file)
file.close()

#fish = [3,4,3,1,2]

#         0 1 2 3 4 5 6 7 8
#count = [0,0,0,0,0,0,0,0,0]
count = eval(fish)

a = count[8]
for i in range(0, 256):
    for j in range(7, -1, -1):
        b = count[j]
        count[j] = a
        a = b
    count[8] = a
    count[6] += a
   
    #print("Day " + str(i + 1) + ": " + str(count))
    #print()

print(str(sum(count)) + "\n")

print("finished in %s seconds" % (time.time() - startTime),"\n")