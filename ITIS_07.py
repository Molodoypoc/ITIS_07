text = open('47100387.txt', 'r')

# Преобразование текста в список слов
words = text.lower().split()

# Создание словаря для подсчета частоты слов 
word_count = {}

# Подсчет частоты слов
for word in words:
    # Удаление символов пунктуации 
    word = word.strip('.,?!:;')
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Вывод результатов
print("Слова и их частота:")
for word, count in word_count.items(): 
    print(f"{word}: {count}")