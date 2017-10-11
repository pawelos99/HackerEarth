def dec_to_base_5(x):
    '''Returns base 5 number from decimal'''
    if x == 0:
        return '0'
    s = ''
    while x:
        s = str(x % 5) + s
        x = x // 5
    return s


def get_number_from_t_zeroes(M):
    '''Returns smallest number which factorial has
    M trailing zeroes.'''
    M_base_5 = dec_to_base_5(M)
    fives = [5**y for y in range(len(M_base_5))]
    sum_fives = sum(fives)
    for f in fives[:-1]:
        # round to 5th decimal place to get rid of small division errors
        value = round(M / sum_fives * f, 5)
        curr_f_val = int(value)
        M -= curr_f_val
        sum_fives -= f
    return M * 5


def get_factorial_trailing_zeroes(M):
    '''Returns the number of trailing zeroes in M factorial'''
    t_zeroes = 0
    power = 1
    while (5**power) <= M:
        t_zeroes += M // (5**power)
        power += 1
    return t_zeroes


T = int(input())
for _ in range(T):
    t_zeroes = int(input())
    M = get_number_from_t_zeroes(t_zeroes)

    # check if creating such a number is possible
    if get_factorial_trailing_zeroes(M) != t_zeroes:
        print(0)
        continue

    print(5)
    print(*[M + x for x in range(5)])
