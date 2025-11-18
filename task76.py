n, m = int(input()), int(input())

# Книги на русском языке
rus_books = {input() for _ in range(n)}

# Для каждой книги в летнем списке проверяем наличие
for _ in range(m):
    book = input()
    if book in rus_books:
        print('YES')
    else:
        print('NO')

