def text_stat(filename):
    # открываю файл в кодировке utf-8 для нормальной работы с кириллицей
    # Если такого файла нет, то возвращаю словарь с ошибкой
    try:
        f = open(filename, encoding='utf-8')
        # Файлы с другим форматом вызывают ошибку при попытке пройтись по строчкам (строка 26)
        if filename[-4:] != '.txt':
            return {'error': 'Ошибка чтения файла - он не txt'}
    except FileNotFoundError:
        return {'error': 'Файл с таким именем не найден'}
    # создаю словарь
    diction = {'word_amount': 0, 'paragraph_amount': 0, 'bilingual_word_amount': 0}
    latin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    kiril = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
             'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
             'к',
             'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
             'ё', 'Ё']
    # заполняю его кириллицей и латиницей (все буквы-ключи имеют значение 0)
    for i in latin + kiril:
        diction[i] = [0, 0]
    letter_num = 0
    # файл читаю построчно
    for line in f:
        # если строка не пустая, то увеличиваю количество абзацев
        if line[0] != '\n':
            diction['paragraph_amount'] += 1
        # 1 слово начинается с 0 индекса
        w_start = 0
        # перебираю индексы строки
        for i in range(len(line) - 1):
            # если вижу конец слова
            if line[i] != ' ' and (line[i + 1] == ' ' or line[i + 1] == '\n'):
                # увеличиваю кол-во слов, запоминаю индекс конца слова, создаю int для подстчёта
                diction['word_amount'] += 1
                w_end = i
                k_num = 0
                l_num = 0
                word = line[w_start:w_end]

                for k in range(len(word)):
                    if word[k] in latin:
                        l_num += 1
                    elif word[k] in kiril:
                        k_num += 1
                    else:
                        # символ не входит в алфавиты - проверять не нужно
                        continue

                    diction[word[k]][0] += 1
                    if word[0:k + 1].count(word[k]) == 1:
                        diction[word[k]][1] += 1
                # проверяю на наличие в слове обоих алфавитов
                if k_num * l_num:
                    diction['bilingual_word_amount'] += 1
                # обновляю начало слова
                w_start = w_end + 1
                # подсчитываю количество букв
                letter_num += k_num + l_num
    # Изменяю количеста на кортежы с частотой и долей, на соответствующий кортеж
    if diction['word_amount'] != 0:
        for i in latin + kiril:
            # считаю доли и округляю до сотых
            diction[i] = (round(diction[i][0] / letter_num, 2), round(diction[i][1] / diction['word_amount'], 2))
    else:
        # Если файл пустой, то и частота, и доля раны 0.
        for i in latin + kiril:
            diction[i] = (0, 0)
    f.close()
    return diction
