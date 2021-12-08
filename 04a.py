def readerInstruct(file):
    line = file.readLine()
    return line

def readerBoards(file):
    return 1

def mark(num, board):
    return

def scan(board):
    return True

#draw the numbers and mark the position then scan
def bingo(instructions, boards):
    for e in instructions:
        for i in range(0, len(boards)):
            mark(e, boards[i])
            if scan(boards[i]):
                return boards[i]







#read the file into an array of numbers and a 3d array for the boards
file = open("Input/input04.txt", "r")
instructions = readerInstruct(file)
print("Instructions: " + str(instructions))
#boards = readerBoards(file)

#Determine the winner by repeatedly marking and scanning the boards

#winner = bingo(instructions, boards)
'''
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
print("Result: " + str(sum(winner) * finalNum))
'''






