a = int(input())
b = int(input())

result = []
for i in range(a, b + 1):
    if i % 3 == 0:
        result.append(i)

print(sum(result) / len(result))
