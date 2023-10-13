from roman_to_dec import to_dec

# Проверка первых 1000 римских чисел
f = open('Rom_table.txt', encoding='utf-8')
roman_and_dec = []
k = []
n = 0
for line in f:
    if n % 2 == 0:
        k.append(line[:-1])
    if len(k) == 2:
        roman_and_dec.append(k)
        k = []
    n += 1
f.close()

print(roman_and_dec)
for pair in roman_and_dec:
    assert to_dec(pair[1]) == int(pair[0]), 'Числа не сошлись'
print('Программа выдаёт верный резальтат на первой тысяче чисел')
