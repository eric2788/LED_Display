EMPTY = " "
BLACK = "#"


def get_led(black: bool):
    return [[BLACK if black else EMPTY for n in range(3)] for x in range(5)]


some = {
    1: {
        "change": [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
        "format": BLACK
    },
    2: {
        "change": [(1, 0), (1, 1), (3, 1), (3, 2)],
        "format": EMPTY
    },
    3: {
        "change": [(1, 0), (1, 1), (3, 0), (3, 1)],
        "format": EMPTY
    },
    4: {
        "change": [(0, 1), (1, 1), (3, 0), (3, 1), (4, 0), (4, 1)],
        "format": EMPTY
    },
    5: {
        "change": [(1, 1), (1, 2), (3, 0), (3, 1), (3, 1)],
        "format": EMPTY
    },
    6: {
        "change": [(1, 1), (1, 2), (3, 1)],
        "format": EMPTY
    },
    7: {
        "change": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
        "format": BLACK
    },
    8: {
        "change": [(1, 1), (3, 1)],
        "format": EMPTY
    },
    9: {
        "change": [(1, 1), (3, 0), (3, 1)],
        "format": EMPTY
    },
    0: {
        "change": [(1, 1), (2, 1), (3, 1)],
        "format": EMPTY
    }
}


def print_led(i: int):
    ss = str(abs(i))
    for s in ss:
        d = int(s)
        if d in some:
            mat = some[d]["format"]
            che = some[d]["change"]
            led = get_led(mat == EMPTY)
            for (x, y) in che:
                led[x][y] = mat
            for l in led:
                for y in l:
                    print(y, end='')
                print('')
            print('')
        else:
            print('none')


print_led(6645)
