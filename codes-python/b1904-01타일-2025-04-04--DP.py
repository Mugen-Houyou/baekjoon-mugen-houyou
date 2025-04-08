import sys
# sys.setrecursionlimit(1<<20)

# def tile_fib_rc(n):
#     if momoi[n]: return momoi[n]
#     momoi[n] = tile_fib(n-1)+tile_fib(n-2)    
#     return momoi[n]

def tile_fib(n):
    for i in range(3,n+1):
        momoi[i] = (momoi[i-1] + momoi[i-2])%15746

    return momoi[n]

momoi = [None]*(1000001)
momoi[0] = 0
momoi[1] = 1
momoi[2] = 2
momoi[3] = 3
momoi[4] = momoi[3] + momoi[2]

print(tile_fib(int(input())))
