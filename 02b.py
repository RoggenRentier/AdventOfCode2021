def reader(file):
    lines = file.readlines()
    arr = [0] * len(lines)
    i = 0
    for i in range(0, len(lines)):
        arr[i] = lines[i]
    return arr

def calcPos(directions):
    #0=horizontal, 1=vertical, 2=aim
    A = [0] * 3
    S = ""

    for i in range(0, len(directions)):
        if(directions[i][0] == 'f'):
            S = directions[i].split()[1]
            A[0] += int(S) 
            A[1] += int(S) * A[2]
        elif directions[i][0] == 'u':
            S = directions[i].split()[1]
            A[2] -= int(S) 
        else:
            S = directions[i].split()[1]
            A[2] += int(S)
    
    return A
            
            


file = open("Input\input02.txt")
#directions = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
directions = reader(file)
position = calcPos(directions)
print(position)
print(position[0] * position[1])