def imts(weight, height):
    imt =  weight/(height*height)
    if imt < 18.5:
        print ('Недостаточная масса')
    elif imt > 25:
        print('Избыточная масса')
    else:
        print('Оптимальная масса')

weight, height = float(input()), float(input())

imts(weight,height)

