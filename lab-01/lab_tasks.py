# def lmbda(text):
#     words = text.split()   # разбиваем строку на слова
#     result = ""

#     for word in words:
#         if len(word) % 2 == 0:
#             # если длина чётная → переворачиваем
#             reversed_word = ""
#             for letter in word:
#                 reversed_word = letter + reversed_word
#             result += reversed_word + " "
#         else:
#             # если нечётная → оставляем как есть
#             result += word + " "

#     return result.strip()

# print(lmbda("hello code hi test"))

text = ["apple", "banana", "cherry", "banana", "apple", "apple" ]

new_words = {}

for word in text:
    if word in new_words:
        new_words[word] += 1
    else:
        new_words[word] = 1

print(new_words)



