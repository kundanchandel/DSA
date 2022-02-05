'''
There are N cells arranged in linear fasion, you are standing at 0th cell, 
and want to reach (n-1)th cell. At each cell you can have 6 possible jumps to make.
Find: In how many ways you can reach to (n-1)th cell, and print ways.
'''
totalPaths = 0

def printPaths(n,start,osf):
    global totalPaths
    if start>=n:
        return
    if start == n-1:
        totalPaths +=1
        print(osf)
        return
    for i in range(1,7):
        printPaths(n,start+i,osf +"->"+str(i))
    
printPaths(7,0,"")
print(totalPaths)
