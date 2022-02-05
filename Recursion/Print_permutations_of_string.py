'''
Given a string, with all unique chars.
print all possible permutations of a string
'''

def printPermutations(string,osf):
    if string == "":
        print(osf)
        return
    s= string
    for i in range(len(s)):
        ros = s[0:i] + s[i+1:]
        printPermutations(ros,s[i]+osf)
        
printPermutations("abc","")
