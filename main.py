
from nim_engine import put_stones, take_from_bunch, get_bunches, is_gameover
from termcolor import cprint

put_stones()
user_number = 1
while True:
    cprint('Текущая позицмя', 'green')
    cprint(get_bunches(), 'green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color = user_color)
    pos = input('Откуда берем? ')
    qua = input('Сколько берем? ')
    step_successed = take_from_bunch(position = int(pos),quantity = int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход', color = 'red')
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1

print('Выиграл игрок номер', user_number)