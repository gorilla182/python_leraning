numbers = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

num = [int(i) for i in input()]

result = []

for digit in num:
    result.append(numbers[digit])
print(*result)