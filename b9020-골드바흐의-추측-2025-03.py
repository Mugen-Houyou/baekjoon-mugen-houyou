def is_prime(num):
    if num<2: return False
    else:
        for i in range(2,int(num**0.5+1)):
            if num%i == 0:
                return False
    return True

for t in range(int(input())):
    inm = int(input())
    for i in reversed(range(2,int(inm/2)+1)):
        if is_prime(i) and is_prime(inm-i):
            print(i, inm-i)
            break
