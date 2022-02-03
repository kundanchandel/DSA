# Given two Nos a and b calculate a**b recursively

# a**b = a * a**(b-1)
def pow(a,b):
    if b == 0:
        return 1
    return a * pow(a,b-1)
    
print(pow(3,3))

# a**b = if b is even a**(b/2) * a**(b/2). If b is odd a * a**(b/2) * a**(b/2)
def optimised_pow(a,b):
    if b==0:
        return 1
    if (b==1):
        return a
    temp = optimised_pow(a,int(b/2)) 
    if(b%2==0):
        return temp*temp
    else:
        return a * temp * temp

print(optimised_pow(3,3),optimised_pow(3,4))
