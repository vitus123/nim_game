from random import randint

MAX_BUNCHRS = 5
MAX_BUNCHRS_SIZE = 20

_holder = {}

def put_stones():
    global _holder
    _holder = {}
    for i in range(1,6):
        _holder[i] = (randint(1, 20))


def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return  False


def get_bunches():
    res =[]
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res


def is_gameover():
    return sum(_holder.values()) == 0

