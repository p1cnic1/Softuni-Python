divisor = int(input())
max_n = int(input())

r = 0

for num in range(1, max_n + 1):
    if num % divisor == 0:
        r = num

print(r)