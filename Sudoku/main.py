Board1 = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

Board2 = [[4,0,0,6,0,2,3,0,0],
          [0,0,0,0,4,0,0,0,6],
          [0,0,0,0,8,0,0,7,4],
          [0,0,0,0,5,0,0,2,0],
          [0,5,6,0,0,0,9,8,0],
          [0,3,0,0,6,0,0,0,0],
          [8,1,0,0,7,0,0,0,0],
          [3,0,0,0,2,0,0,0,0],
          [0,0,7,3,0,4,0,0,8]]



def outputBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def searchBlank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return (i,j) 
    return None

def isValid(board, num, pos):
    #Column Check
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #Row Check
    for i in range (len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Sqaure Check
    x = pos[1] // 3
    y = pos[0] // 3
    
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if(board[i][j] == num and (i,j) != pos):
                return False
            
    return True

def solve(board):
    blank = searchBlank(board)
    if not blank:
        return True
    else:
        row, col = blank
    
    for i in range(1,10):
        if isValid(board, i, (row,col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False

print("Unsolved Board: ")
outputBoard(Board2)
solve(Board2)
print("Solved Board: ")
outputBoard(Board2)
            


    

    
    
    

            
