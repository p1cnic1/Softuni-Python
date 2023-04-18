factor = int(input())
count = int(input())

result = []

for i in range(1 , count + 1):
    nums = i * factor
    result.append(nums)

print(result)