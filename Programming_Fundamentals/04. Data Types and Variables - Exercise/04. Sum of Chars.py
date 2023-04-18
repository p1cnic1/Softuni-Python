first = int(input())
result = 0

for _ in range(first):
    symbol = input()
    result += ord(symbol)

print(f'The sum equals: {result}')