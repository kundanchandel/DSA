temp = []

def printPers(arr,i,n):
    if(i==n):
        for a in temp:
            print(a,end=" ")
        print()
        return
    
    temp.append(arr[i])
    printPers(arr,i+1,n)
    temp.pop()
    printPers(arr,i+1,n)

printPers([1,2,3],0,3)
            
