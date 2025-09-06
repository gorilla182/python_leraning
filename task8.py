

def counter():
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    fourth_cnt = 0

    dot_cnt = int(input())
    for i in range(dot_cnt):
        dots_list = []
        dots = input()
        dots_list = dots.split(' ')
        if int(dots_list[0]) > 0 and int(dots_list[1]) > 0:
            first_cnt += 1
        elif int(dots_list[0]) < 0 and int(dots_list[1]) > 0:
            second_cnt+= 1
        elif int(dots_list[0]) < 0 and int(dots_list[1]) < 0:
            third_cnt += 1
        elif int(dots_list[0]) > 0 and int(dots_list[1]) < 0:
            fourth_cnt+=1
    print('Первая четверть:', first_cnt)
    print('Вторая четверть:', second_cnt)
    print('Третья четверть:', third_cnt)
    print('Четвертая четверть:', fourth_cnt)








counter()
