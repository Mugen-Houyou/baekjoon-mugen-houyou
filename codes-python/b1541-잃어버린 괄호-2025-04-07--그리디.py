import sys

input_str = sys.stdin.readline().strip()

parts = [sum(int(numbers) for numbers in p.split("+")) for p in input_str.split("-")]

result = parts[0]

for i in range(1,len(parts)):
    result -= parts[i]

print(result)
