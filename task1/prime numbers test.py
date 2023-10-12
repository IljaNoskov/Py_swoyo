from just_number import prime_numbers

# Берём из интернета массив простых чисел от 1 до 100000
# Сайт-источник https://1cov-edu.ru/calc/tablitsa-prostyh-chisel/?n1=1&n2=100000&separator=%20
f = open('prime_numbers 1-100000.txt')
true_prime_numbers = f.read().split()
for i in range(len(true_prime_numbers)):
    true_prime_numbers[i] = int(true_prime_numbers[i])
f.close()

# Генерируем свой массив чисел в заданном диапазоне
my_prime_numbers = prime_numbers(1, 100000)

# Проверяем на равенство результатов
# В цикле, чтобы узнать, в каких элементаи не совпадение
for i in range(max(len(true_prime_numbers), len(my_prime_numbers))):
    assert my_prime_numbers[i] == true_prime_numbers[
        i], f'Массивы не равны! Ошибка в элементе с индексом {i}, {my_prime_numbers[i]} != {true_prime_numbers[i]}'
print('Массивы одинаковы')
