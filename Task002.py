# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

# import os
# print(os.name)
import os                      # Модуль os  это библиотека функций для работы с операционной системой.получать доступ к переменным окружения, управлять директориями и файлами:
def encode_file(my_text):  
    str_code = ''
    count = 1       
    for i in range(len(my_text)):
        if i < len(my_text)-1:
            if my_text[i] == my_text[i + 1]:
                count += 1
            else:
                str_code += str(count) + my_text[i]
                count = 1
        else:
            str_code += str(count) + my_text[i]
    return str_code



def decode_file(strc):
    count = ''
    result = ''
    for i in strc:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(f'текст: \n{text}')
with open('decode.txt', 'w') as data:
    data.write(text)

with open('decode.txt', 'r') as data:
    my_text = data.read()

strc = encode_file(my_text)
print(f'Сжатый текст: \n{strc}')                     # Проверка текста

with open('code2.txt', 'w') as data:
    data.write(strc)

with open('code2.txt', 'r') as data:
    my_text = data.read()

total = decode_file(my_text)
print(f'Восстановленный текст: \n{total}')            # проверка текста

with open('decode.txt', 'w') as data:
    data.write(total)