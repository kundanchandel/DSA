'''
Given a string, with all chars.
print all possible permutations of a string
'''

def printPermutations(string,osf):
    if string == "":
        print(osf)
        return
    s= string
    tempSet = set()
    for i in range(len(s)):
        if(s[i] not in tempSet):
            ros = s[0:i] + s[i+1:]
            printPermutations(ros,s[i]+osf)
            tempSet.add(s[i])
        
printPermutations("abc","")
