def isArraySorted(array,startIndex):
    if startIndex == len(array)-1:
        return True
    isSorted = isArraySorted(array,startIndex+1)
    return isSorted and array[startIndex]<=array[startIndex+1]

print(isArraySorted([1,2,2,5,3],0))
