memo=[None]*100
counter=0
def fib(n):
    global counter
    counter+=1
    if memo[n] is not None:
        return memo[n]
    if n==0 or n==1:
        return n
    memo[n]= fib(n-1)+fib(n-2)
    return memo[n]
    
print(fib(20))
print(counter) #counter shows how many times the function has to be called. Highly inefficient. O(2^n).

