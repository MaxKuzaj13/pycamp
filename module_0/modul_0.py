from random import randint


def draw_number():
    drew = []
    while len(drew) < 6:
        x = randint(1, 50)
        if not x in drew:
            drew.append(x)
    return drew


if __name__ == '__main__':
    print('Test')
    count_weeks = 0
    my_set = {1, 13, 17, 9, 49, 21}
    while True:
        draw_list = draw_number()
        if my_set == set(draw_list):
            print(f'Udało się, potrzeba było {count_weeks} tygodni czyli {count_weeks // 52} lat i {count_weeks % 52} tygodni')
            break
        else:
            print(f' count week {count_weeks} numbers: {draw_list}')
            count_weeks += 1
