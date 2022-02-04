# Givem an array, Print all subsets

def printSubset(array,currentIdx,OSF):
    if currentIdx == len(array):
        print("[" +OSF+"]")
        return
    printSubset(array,currentIdx + 1, OSF + str(array[currentIdx])+",")
    printSubset(array,currentIdx + 1, OSF)
    
printSubset([1,2,3],0,"")
