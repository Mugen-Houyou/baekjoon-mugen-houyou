# result = 0

# def hanoi(n, src, tmp, dest):
#     global result
#     if n == 1:
#         print(f'{src} {dest}')
#         result += 1
#         return
#     hanoi(n-1, src, dest, tmp)
#     print(f'{src} {dest}')
#     result += 1
#     hanoi(n-1, tmp, src, dest)

# n = int(input())
# hanoi(n, 1, 2, 3)
# print(result)

def hanoi(n, src, tmp, dest):
    if n == 1:
        print(f'{src} {dest}')
        return
    hanoi(n-1, src, dest, tmp)
    print(f'{src} {dest}')
    hanoi(n-1, tmp, src, dest)

n = int(input())
print(2**n-1)
if n<=20: 
    hanoi(n, 1, 2, 3)