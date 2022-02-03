# There are N persions who wants to go to the party, they can either go alone or can go into a pair. Calculate no of ways in which N persions can goto the party.

# SOl
# a,b,c,d...... N persions
# BASE CASE for N = 1, return 1
# BASE CASE for N = 2 return 2

# Recursive assumption, Out of N persion A has 2 ways,
# Either go alone or go in pair
# If A goes alone no of ways is equals to f(N-1).

# If a goes in a pair, total ways will be N-1 * f(N-2)
# as A block one more persion for pairing.


def calculateWays(n):
    return n if n<3 else calculateWays(n-1) + (n-1) *calculateWays(n-2)

    
print(calculateWays(4))
