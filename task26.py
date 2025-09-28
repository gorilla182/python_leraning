new_list = input().split()
splits = [[]]

for i in range(len(new_list)):
    for j in range(i + 1, len(new_list) + 1):
        splits.append(new_list[i:j])

print(splits)