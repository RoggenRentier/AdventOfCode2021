import copy

def readerInstruct(file):
    line = file.readline()
    line = line.split(",")
    for i in range(0, len(line)):
        line[i] = int(line[i])
    return line


def readerBoards(file):
    boards = [[[0]*5 ]*5 ]*100
    boardArr = [0] * 10000
    i = 0
    file.readline()
    line = file.readline()
    while line:
        line = line.replace("\n", "")
        if not line:
            #print("isEmpty")
            pass
        else:
            helpArr = toArray(line)
            for e in helpArr:
                print(e)
                boardArr[i] = e
                i += 1
    
    print(boardArr)
    
    
    '''
    boards = [[[0]*5 ]*5 ]*100
    i = 0 
    j = 0

    file.readline()
    line = file.readline()

    while line:
        line = line.replace("\n", "")
        #print(line)
        #if line.isspace() or line:  #basically isempty()
        #if len(line.strip()) == 0:
        if not line:
            #print("isEmpty")
            pass
        else:
            #print("notEmpty")
            
            boards[i][j] = copy.deepcopy(toArray(line))
            print(boards[i][j])
            j += 1
            if j == 5:
                j = 0
                i += 1
            
            boards[i] = toBoard(toArray)


        line = file.readline() 
    
    return boards
    '''






def toArray(line):
    arr = line.split(" ")
    #print(arr)
    i = 0
    #for i in range(0, len(arr)):
    while i < 5:
        if len(arr[i].strip()) == 0:
            arr.pop(i)
        else:
            #print(arr[i])
            arr[i] = int(arr[i])
            i += 1
    return arr





def mark(num, board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == num:
                board[i][j] = -1
    return board


def scan(board):
    #horizontal
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] != -1:
                break
            if j == len(board[0]) - 1:
                return True

    #vertical
    for j in range(0, len(board[0])):
        for i in range(0, len(board)):
            if board[i][j] != -1:
                break
            if i == len(board) - 1:
                return True    
    return False

#draw the numbers and mark the position then scan
def bingo(instructions, boards):
    for e in instructions:
        for i in range(0, len(boards)):
            mark(e, boards[i])
            if scan(boards[i]):
                return boards[i]

def sum(board):
    finSum = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] != -1:
                finSum += board[i][j]
    return finSum






#read the file into an array of numbers and a 3d array for the boards
file = open("c:/Users/cedri/Documents/Python/Git/AdventOfCode2021/Input/input04.txt")
instructions = readerInstruct(file)
print("Instructions: " + str(instructions))
print()


boards = readerBoards(file)
file.close()

#instructions = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#boards = [[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]], [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]]
#testBoard = [[22, 13, -1, 11, 0], [8, 2, -1, 4, 24], [21, 9, -1, 16, 7], [6, 10, -1, 18, 5], [1, 12, -1, 15, 19]]
'''
#print(instructions)
print()
print("-----------------")
print()
for e in boards:
    print()
    print(e)
print()

#Determine the winner by repeatedly marking and scanning the boards



winner = []
finalNum = -1

for e in instructions:
    for i in range(0, len(boards)):
        boards[i] = mark(e, boards[i])
        if scan(boards[i]):
            winner = boards[i]
            finalNum = e
            break
    if len(winner) > 0:
        break

print()
print("Winner: " + str(winner))
print("FinalNum: " + str(finalNum))
print("Result: " + str(sum(winner) * finalNum))

'''





