# You are given a 2D matrix of n*m. You will start at top left and want to goto the bottom right. At each point you can either go right or down. Print all possible path.

totalPath = 0

def printMazePaths(r,c,cr,cc,osf):
    global totalPath
    if cr>r or cc>c:
        return
    if cr==r-1 and cc==c-1:
        totalPath +=1
        print(osf)
        return
    printMazePaths(r,c,cr+1,cc, osf + "R ")
    printMazePaths(r,c,cr,cc+1, osf + "D ")
    
    
        
printMazePaths(3,3,0,0,"")
print(totalPath)

# You are given a 2D matrix of n*m. You will start at top left and want to goto the bottom right. At each point you can either go right or down or diagonal. Print all possible path.

totalPathWithDiagonal = 0

def printMazePathsWithDiagonal(r,c,cr,cc,osf):
    global totalPathWithDiagonal
    if cr>r or cc>c:
        return
    if cr==r-1 and cc==c-1:
        totalPathWithDiagonal +=1
        print(osf)
        return
    printMazePathsWithDiagonal(r,c,cr+1,cc, osf + "R ")
    printMazePathsWithDiagonal(r,c,cr,cc+1, osf + "D ")
    printMazePathsWithDiagonal(r,c,cr+1,cc+1, osf + "Dg ")
    
    
        
printMazePathsWithDiagonal(3,3,0,0,"")
print(totalPathWithDiagonal)
