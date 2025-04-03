import sys

ABOUT_MAX = 1<<31
ABOUT_MIN = -1<<31  

print(123, sys.getsizeof(123))                # 28 bytes (헤더 24 bytes + digit 1개)
print(1 << 30, sys.getsizeof(1 << 30))        # 32 bytes (헤더 24 bytes + digit 2개)
print(1 << 31, sys.getsizeof(1 << 31))        # 32 bytes (헤더 24 bytes + digit 2개)
print(1 << 32, sys.getsizeof(1 << 32))        # 32 bytes (헤더 24 bytes + digit 2개)
print(1 << 33, sys.getsizeof(1 << 33))       # 32 bytes (헤더 24 bytes + digit 2개)
print(1 << 34, sys.getsizeof(1 << 34))       # 32 bytes (헤더 24 bytes + digit 2개)
print(1 << 60, sys.getsizeof(1 << 60))        # 32 bytes (헤더 24 bytes + digit 2개)
print(-1 << 60, sys.getsizeof(-1 << 60))      # 36 bytes (헤더 24 bytes + digit 3개)
                                              # 참고: CPython 기준입니다.
exit()
