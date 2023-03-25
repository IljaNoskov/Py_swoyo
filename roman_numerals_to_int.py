def to_dec(rom):
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    # на старте десятичное число равно нулю
    dec = 0
    # перебираем все пары из словаря
    for i, r in all_roman:
        # пока римское число начинается буквы из словаря
        while rom.startswith(r):
            # увеличиваем десятичное число на соответствующее значение из словаря
            dec += i
            # убираем найденную букву из римского числа
            rom = rom[len(r):]
    # как все циклы закончились — возвращаем десятичное число
    return dec

#Проверка первых 1000 римских чисел
f=open('Rom_table.txt',encoding='utf-8')
mas=[]
k=[]
n=0
for line in f:
    if n%2==0:
        k.append(line[:-1])
    if len(k)==2:
        mas.append(k)
        k=[]
    n+=1
f.close()

print(mas)
for i in mas:
    if to_dec(i[1])!=int(i[0]):
        print('Error')
    
