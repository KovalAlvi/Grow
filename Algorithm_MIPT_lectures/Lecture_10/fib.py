import matplotlib.pyplot as plt

def find_fib(N):
    fib = [0,1] + [0]*(N-1)
    for i in range(2, N+1):
        fib[i] = fib[i-1] + fib[i-2]
    #return fib[N], fib
    return fib[N]

A = find_fib(5)
print(A)
