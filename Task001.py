# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect

# txt = input("Введите слова через пробел: ")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]# обьявляем список пробегаем по нему и разделяе с помощью split() пустая строка это пробел. если там есть абв не закидываем в список.
# print(f'Результат: {" ".join(lst)}')               #Метод джоин превращает список в строку f - форматирование строки

from random import sample

def random_words(count:int, alp: str = "абв"):        # count: int крутимся нужное количество раз
    words_list = []
    for i in range(count):
        letters = sample(alp, 3)                      #sample apl - указывает сколько будет букв в наборе.
        words_list.append("".join(letters))           # список полученных буковок мы склеиваем с помощью join
    return " ".join(words_list)

def correcting_gaps(words: str) -> str:
    return words.replace("абв", "")
all_list = random_words(int(input("Введите число: ")))
print(all_list)
print(correcting_gaps(all_list))