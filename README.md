# Тестовое задание python. Выполнил Носков Илья.
### Простые числа в заданном диапазоне
Функция поиска простых чисел в диапазоне
```python
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

```
Проверка числа на простоту
```python
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
```

#####Реализация проверки
В файле с окончанием test реализована проверка функции - мы берём массив простых чисел в промежутке от 1 до 100000 (взятый из интернета) и сверяем с тем, что получился у нас. 
``` python
from prime_number import prime_numbers

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
```

### Анализ текста
```python
def text_stat(filename):
    #открываю файл в кодировке utf-8 для нормальной работы с кириллицей
    f=open(filename,encoding='utf-8')
    #создаю словарь
    diction={'word_amount':0,'paragraph_amount':0,'bilingual_word_amount':0}
    latin=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    kiril=['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
           'Х','Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы','Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
           'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё', 'Ё']
    #заполняю его кириллицей и латиницей
    for i in latin:
        diction[i]=0
    for i in kiril:
        diction[i]=0
    #файл читаю построчно
    for line in f:
        #если строка не пустая, то увеличиваю количество абзацев
        if line[0]!='\n':
            diction['paragraph_amount']+=1
        # 1 слово начинается с 0 индекса
        w_start=0
        # перебираю индексы строки
        for i in range(len(line)-1):
            # если вижу конец слова
            if line[i]!=' ' and (line[i+1]==' ' or line[i+1]=='\n'):
                #увеличиваю кол-во слов, запоминаю индекс, создаю сеты для кириллицы и латиницы
                diction['word_amount']+=1
                w_end=i
                k_word=set()
                l_word=set()
                #заново иду по всему слову
                for k in range(w_start,w_end+1):
                    # добавляю кириллицу и латиницу в сеты
                    if line[k] in latin:
                        l_word.add(line[k])
                    elif line[k] in kiril:
                        k_word.add(line[k])
                # добавляю из сетов в словарь
                for k in l_word:
                    diction[k]+=1
                for k in k_word:
                    diction[k]+=1
                #проверяю на наличие в слове обоих алфавитов
                if len(k_word)*len(l_word):
                    diction['bilingual_word_amount']+=1
                # обновляю начало слова
                w_start=w_end+1
    #Изменяю количество слов с буквой, на соответствующий кортеж
    if diction['word_amount']!=0:
        for i in latin:
            diction[i]=(diction[i],diction[i]/diction['word_amount'])
        for i in kiril:
            diction[i]=(diction[i],diction[i]/diction['word_amount'])
    else:
        for i in latin:
            diction[i]=(0,0)
        for i in kiril:
            diction[i]=(0,0)
    f.close()
    return diction
```

#####Реализация проверки
Проверка кода реализована вручную. Есть файл text.txt, в котором лежит стихотворение пушкина, с изменёнными словами (в них добавили английские буквы)

### Перевод из римской системы в десятичную
Для того, чтобы понять алгоритм нужно знать о римских числах. В них все "цифры" идут по убыванию, если считать сочетания с уменьшающим концом за одну цифру. При чём такое сочетание может быть только первой "цифрой" в числе. По этому мы можем всего 1 раз пройтись по массиву римких чисел, переводя каждую цифру в десятичную систему и складывая её с продидущим результатом. Эту информацию о римских чисел брал с сайта https://www.sravni.ru/text/rimskie-czifry/?upd
```python
def to_dec(rom):
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
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
```

#####Реализация проверки
В качестве проверки просто сравниваю результаты функции с "таблицей" Римских чисел от 1 до 1000. "Таблица" лежит в файле Rom_table.txt.
```python
#Проверка первых 1000 римских чисел
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

```
