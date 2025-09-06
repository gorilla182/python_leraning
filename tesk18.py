b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

word = input() + ' запретил букву'


for i in range (len(b)):
    if b[i] in word:
        print(word, b[i])
        word = word.replace(b[i], '')
        word = " ".join(word.split())
