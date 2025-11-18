data = [int(i) for i in input().split()]

filtred_data = set()

duplicate_data = 0

for i in data:
    len_data = len(filtred_data)
    filtred_data.add(i)
    if len(filtred_data) > len_data:
        continue
    else:
        duplicate_data += 1
print(duplicate_data)

