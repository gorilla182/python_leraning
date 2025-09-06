res = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']

timur = input()
ruslan = input()

if timur == ruslan:
    print("ничья")
else:
    timur_idx = res.index(timur)
    ruslan_idx = res.index(ruslan)

    # Определяем разницу по модулю 5 (циклический список)
    diff = (timur_idx - ruslan_idx) % 5

    if diff in [1, 3]:
        print("Руслан")  # Тимур побеждает
    else:
        print("Тимур")  # Руслан побеждает