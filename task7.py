def formats(number):
    number = str(number)
    if len(number) == 4:
        numbers = list(number)
        numbers.insert(1,',')
        return ''.join(numbers)
    elif len(number) == 5:
        numbers = list(number)
        numbers.insert(2, ',')
        return ''.join(numbers)
    elif len(number) == 6:
        numbers = list(number)
        numbers.insert(3, ',')
        return ''.join(numbers)
    elif len(number) == 7:
        numbers = list(number)
        numbers.insert(1, ',')
        numbers.insert(5, ',')
        return ''.join(numbers)
    elif len(number) == 8:
        numbers = list(number)
        numbers.insert(2, ',')
        numbers.insert(6, ',')
        return ''.join(numbers)
    elif len(number) == 9:
        numbers = list(number)
        numbers.insert(3, ',')
        numbers.insert(7, ',')
        return ''.join(numbers)
    elif len(number) == 10:
        numbers = list(number)
        numbers.insert(1, ',')
        numbers.insert(5, ',')
        numbers.insert(9, ',')
        return ''.join(numbers)
    elif len(number) == 11:
        numbers = list(number)
        numbers.insert(2, ',')
        numbers.insert(6, ',')
        numbers.insert(10, ',')
        return ''.join(numbers)
    elif len(number) == 12:
        numbers = list(number)
        numbers.insert(3, ',')
        numbers.insert(7, ',')
        numbers.insert(11, ',')
        return ''.join(numbers)
    elif len(number) == 13:
        numbers = list(number)
        numbers.insert(1, ',')
        numbers.insert(5, ',')
        numbers.insert(9, ',')
        numbers.insert(13, ',')
        return ''.join(numbers)
    elif len(number) < 4:
        return number


n = int(input())
print(formats(n))
