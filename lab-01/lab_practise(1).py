# def top_k_words(text, k):
#    

# TASK 6
# def func(text):
#     cleaned = ""
#     lst = []
    

#     for word in text:
#         if word != " ":
#             cleaned += word
#         else:
#             lst += [word]
#             cleaned = ""

#     if cleaned != "":
#         lst += [word]


#     numbers = "1234567890"
#     set_word = set()


#     for ch in lst:
#         if ch not in numbers:
#             set_word.add(ch)
#         else:
#             set_word += 0

#     return set_word

# print(func("abc123 Computer diffrent usually hardly ever"))


# TASK 9
# def alternate_case_blocks(text, n):
#     result = ""
#     for i in range(0, len(text), n):
#         block = text[i:i+n]
#         if (i // n) % 2 == 0:
#             result += block.upper()
#         else:
#             result += block.lower()
#     return result
# alternate_case_blocks("abcdefghijklmnopqrstuvwxyz", 5)
            
# TASK 12

# def filter_text(text):
#     insame = []
#     notpali = []
#     longerthan3 = []

#     for i in text:
#         if len(i) > 3 and i[0].lower() == i[-1].lower():
#             insame.append(i)
#         if len(i) > 3 and i.lower() != i.lower()[::-1]:
#             notpali.append(i)
#         if len(i) > 3:
#             longerthan3.append(i)
#     return list(set(insame + notpali + longerthan3))

# text = ["exit", "exe", "ciaoamigoc"]
# print(filter_text(text))

# TASK 15
# def word_pattern_sort(text):
#     group = []
#     vowels = "aeiou"
#     word = ""

#     for ch in text:
#         if ch != " ":
#             word += ch
#         else:
#             group += [word]
#             word = ""
        
#     result = []

#     for i in range(len(group)):
#         for j in range(i + 1, len(group)):
#             if group[i] == group[j] or(
#                 group[j] == group[j]
#             ):
#                 result += [group]

#     return result

# print(word_pattern_sort("abcd narxoz universiry push letter items"))

# TASK 18
# def flatten_and_fillter(lst):
#     res = []
#     for i in lst:
#         if i > 0 and i % 4 != 0 and len(str(abs(i))) > 1:
#             res.append(i)
#     return res


# lst = [12, 3, 432, 75, 436, 2, 351, 64, -2, -24]
# print(flatten_and_fillter(lst))

# print(flatten_and_filter([1,"a",3,4,5,6,7,8,9]))

# TASK 21
# def list(w):
#     res = []
#     for i in w:
#         if i.isalpha() and len(i) > 4 and len(i) == len(set(i)):
#             res.append(i.upper())
#     return res

# w = ["apple", "hola", "judge", "hi", "no", "yes", "da1", "da2"]
# print(list(w))

#24
# def longest_increasing_sublist(nums):


# TASK 27
# def sort_strings(strings):
#     a = strings[:]

#     for i in range(len(a)):
#         for j in range(len(a) - 1):
#             if len(a[j]) < len(a[j + 1]) or (
#                 len(a[j]) == len(a[j + 1]) and a[j] > a[j + 1]):
#                 a[j], a[j + 1] = a[j + 1], a[j]

#     return a[:5]
# strings = ["JBI", "ckslv", "cdsnjceowq", "nwlkqvnkrq;iv", "venjiv", "gew", "gqege", "geg", "wgreg"]
# print(sort_strings(strings))





    




                

            



        





