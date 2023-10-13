def prime_numbers(low, high):
    # создаём пустой список
    p_list = []
    # учитываем только неотрицательные числа
    if low < 0:
        low = 0
    # проверяем каждое число из диапазона на простоту
    for i in range(low, high + 1):
        if is_prime(i) and i != 1:
            p_list.append(i)
    return p_list


def is_prime(num):
    # отдельно проверяем двойку
    if num == 2:
        return True
    # рассчитываем число, до которого есть смысл проверять (корень из числа)
    n = round(pow(num, 1 / 2))
    # проверяем на делимость все числа от 2 до n - корня
    for k in range(2, n + 1):
        if num % k == 0:
            return False
    # если прошли все числа и не встретили делителя, то число простое
    return True
