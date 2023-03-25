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

print(text_stat('text.txt'))
