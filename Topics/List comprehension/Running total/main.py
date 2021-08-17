sequence = input()

result = [int(i) for i in sequence]
result_2 = [result[n] + sum(result[:n]) for n in range(len(result))]
print(result_2)