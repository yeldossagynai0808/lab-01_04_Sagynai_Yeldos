# 1-task
# def analyze_text(text):

#     alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзфывапролдячсмитьЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬ"
#     vowels = "aeiouаеёуоыиэюя"

#     new_word = ""

#     for char in text:
#         if char in alphabet:
#             new_word += char


#     count_vowels = []

#     for char in text:
#         if char in vowels:
#             count_vowels += char

#     if len(new_word) > 5:
#         if new_word[0] == new_word[-1]:
#             return new_word, count_vowels

#     return new_word, count_vowels


# print(analyze_text("Hello World!", "asdkjaksjdl"))


# task-2

# def lmbda(text):

#     words = text.split()
#     result = " "

#     for word in words:
#         if len(word) % 2 == 0:
#             reversed_word = ""
#             for letter in word:
#                 reversed_word = letter + reversed_word
#             result += reversed_word + " "
#         else:
#             result += word + " "


#     return result.strip()

# print(lmbda("hello hi test"))


# task-2(build)
# process = lambda text: " ".join(
#     filter(
#         lambda word: len(word) % 2 == 0,
#         map(
#             lambda word: word[::-1],
#             filter(
#                 lambda word: not any(char.isdigit() for char in word),
#                 text.split()
#             )
#         )
#     )
# )
# print(process("hello hi test h3llo code123 even"))


# task 3
# def top_k_words(text,k):

#     text = text.lower()

#     cleaned_text = ""
#     for char in text:
#         if char.isalpha() or char == " ":
#             cleaned_text += char

#     without_dot = cleaned_text.split()

#     count = {}

#     for letter in without_dot:
#         if letter in count:
#             count[letter] += 1
#         else:
#             count[letter] = 1

#     items = []
#     for word in count:
#         items.append([word, count[word]])

#     for i in range(len(items)):
#         for j in range(len(items)-1):
#             if items[j][1] < items[j+1][1]:
#                 items[j], items[j+1] = items[j+1], items[j]
#             elif items[j][1] == items[j+1][1]:
#                 if items[j][0] > items[j+1][0]:
#                     items[j], items[j+1] = items[j+1], items[j]

#     result = []
#     for i in range(k):
#         if i < len(items):
#             result.append(items[i][0])

#     return result

# print(top_k_words("hello hello apple banana banana apple hi code", 2))


# task-4
# filter_words = lambda text: " ".join(
#     map(
#         lambda w: w.lower(),
#         filter(
#             lambda w: (
#                 sum(1 for c in w if c.isupper())
#                 and not w[0].isupper()
#                 and not w[-1].isupper()
#             ),
#             text.split()

#         )
#     )
# )


# task - 5
# def compress_text(text):
#     if not text:
#         return ""

#     result = ""
#     current_char = text[0]
#     count = 1

#     for char in text[1:]:
#         if char.lower() == current_char.lower():
#             count += 1
#         else:
#             if count > 1:
#                 result += current_char + str(count)
#             else:
#                 result += current_char

#             current_char = char
#             count = 1

#     if count > 1:
#         result += current_char + str(count)
#     else:
#         result += current_char

#     return result

# print(compress_text("aaBBcDDD"))

# print(filter_words("heLlo Hello hellO HeLLo goOd GooD tESt test"))


# task 6
# def lmbda(text):
#     words = text.split()
#     lst = []

#     for word in words:
#         if len(word) > 4 and len(set(word)) == len(word) and not any(c.isdigit() for c in word):
#             lst.append(word)
#     return lst

# print(lmbda("hello world text vid oop cat dog animal"))


# task 7

# def palindrome_words(text):
#     clean_text = ""
#     for char in text:
#         if char.isalpha() or char == " ":
#             clean_text += char.lower()

#     words = clean_text.split()

#     palindromes = []

#     for word in words:
#         if len(word) >= 3 and word == word[::-1]:
#             if word not in palindromes:
#                 palindromes.append(word)

#     palindromes.sort()
#     palindromes.sort(key=len, reverse = True)

#     return palindromes

# print(palindrome_words("hello join next kezek kazak "))

# task 8
# lmbda_func = lambda text: " ".join(
#     "VOWEL" if word[0].lower() in "aeiou" else
#     "CONSONANT" if word.isalpha() else
#     word
#     for word in text.split()
# )

# print(lmbda_func("hello world ice cream idea popcorn 123go"))


# task 9
# def alternate_case_blocks(text,n):
#     result = ""
#     clean = ""

#     for char in text:
#         if char != " ":
#             clean += char

#     block_number = 1

#     for i in range(0,len(clean), n):

#         block = ""

#         for j in range(i, i + n):
#             if j >= len(clean):
#                 break

#             letter = clean[j]

#             if block_number % 2 == 0:

#                 if "a" <= letter <= "z":
#                     letter = chr(ord(letter) - 32)

#             else:

#                 if "A" <= letter <= "Z":
#                     letter = chr(ord(letter) + 32)

#             block += letter

#         result += block
#         block_number += 1

#     return result

# print(alternate_case_blocks("Hello word text alternative", 4))

# task 10
# count_words = lambda text: sum(
#     1 for word in text.split()
#     if len(word) >= 5
#     and not word[0].isdigit()
#     and any(char.isdigit() for char in word)
# )
# print(count_words("hello world test12 abc3d 123abc"))

# task 11
# def common_unique_chars(s1,s2):
#     result = ""
#     digits = "0123456789"

#     for char in s1:
#         if char == " " or char in digits:
#             continue

#         if char in s2 and char not in result:
#             result += char

#     return result

# print(common_unique_chars("hello world 123", "yellow bird"))

# task 13
# def replace_every_nth(text, n , char):
#     result = ""
#     numbers = '0123456789'
#     count = 0

#     for i in range(len(text)):

#         if text[i] != " ":
#             count += 1
#         else:
#             count = 0

#         if (i + 1) % 2 == 0 and text[i] != " " and text[i] not in numbers and count > 3:
#             result += char
#         else:
#             result += text[i]

#     return result

# print(replace_every_nth("hello world 12 dog", 3, "*"))


# task 14
# def lmbda(f):

#     vowels = "aeiou"
#     result = []

#     words = f.split()
#     for word in words:

#         if len(set(word)) <= 3:
#             continue

#         seem = ""
#         ok = True

#         for char in word:
#             if char in vowels:
#                 if char in seem:
#                     ok = False
#                 seem += char

#         if ok :
#             result.append(word)

#     return ",".join(result)


# print(lmbda("Hello world join game"))


#task 15
# def word_pattern_sort(text):
#     vowels = "aeiou"
#     lst = []
#     words = ""

#     for ch in text:
#         if ch != " ":
#             words += ch
#         else:
#             lst += [words]
#             words = ""

#     if words != "":
#         lst += [words]

#     groups = {}

#     for gr in lst:
#         length = len(gr)

#         if length not in groups:
#             groups[length] = []

#         groups[length] += [gr]
    
#     def count_number(word):
#         count = 0

#         for ch in word:
#             if ch.lower() in vowels:
#                 count += 1
#         return count




#     for length in groups:
#         groups[length].sort(key=lambda x: (-count_number(x), x))

#     result = []
#     for length in sorted(groups):
#         for word in groups[length]:
#             result += [word]


#     return result
# print(word_pattern_sort("hello world apple dog banana"))

#task 16
# def transform_list(nums):
#     lst = []

#     for  num in nums:
#         if num >= 0:
#             lst += [num]
#             if num % 2 == 0:
#                 lst = [num ** 2]
                
#             elif num % 2 == 1 and num > 10:
#                 sum_digits = sum(int(d) for d in str(num))
#                 lst += [sum_digits]

#             else:
#                 lst +=  [num]

#     return lst

#task 17
# nums = [3,5,15,123,1245,7]

# filtered = filter(lambda x: ((x % 3 == 0 or x % 5 == 0)
#                             and x % 15 != 0
#                             and len(str(x)) % 2 == 1), nums)

# result = list(map(lambda x: x ** 2, filtered))

# print(result)

#task 18
# def flatten_and_filter(lst):
#     result = []

#     for item in lst:
#         if type(item) == list:
#             result += flatten_and_filter(item)
#         else:
#             if item > 0 and item % 4 != 0 and item >= 10:
#                 result = result + [item]

#         for i in range(len(result)):
#             for j in range(len(result), i + 1):
#                 if result[i] > result[j]:
#                     result[i], result[j] = result[j],result[i]



#     return result

# data = [1, 2, 3, [4, 5, [12, 15]], 20, [25]]
# print(flatten_and_filter(data))
            
#task 19
# lst = lambda a, b: [x for x, y in zip(a, b) if x == y and x % 2 == 0]
# a = [2, 3, 4, 6]
# b = [2, 5, 4, 7]

# print(lst(a, b))

#task 20
# def max_subarray_sum(nums,k):
#     max_sum = None

#     for i in range(len(nums) - k + 1):
#         sub = nums[i: i+k]
#         if all(x > 0 for x in sub):
#             s = sum(sub)
#             if max_sum is None or s > max_sum:
#                 max_sum = s

#     return max_sum

# nums = [1,2,3,4,-1,5]
# k = 2
# print(max_subarray_sum(nums, k))
            
#task 21
# lmbda = lambda lst: list(
#     map(str.upper,
#         filter(lambda w: len(w) > 4 and w.isalpha() and len(set(w)) == len(w), lst)
#     )
# )
# print(lmbda(["Hello", "world","apple", "train", "abcde"]))

#task 22
# def group_by_parity_and_sort(nums):
#     even = []
#     odd = []

#     for n in nums:
#         if n % 2 == 0:
#             even += [n]
#         else:
#             odd += [n]

#     for i in range(len(even)):
#         for j in range(i + 1,len(even)):
#             if even[i] > even[j]:
#                 even[i], even[j] = even[j], even[i]

#     for i in range(len(odd)):
#         for j in range( i + 1, len(odd)):
#             if odd[i] > odd[j]:
#                 odd[i], odd[j] = odd[j], odd[i]

#     result = even + odd

#     return result

# print(group_by_parity_and_sort([1,2,3,4,5,6]))

#task 23
# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))

# f = lambda nums:[
#     nums[i]
#     for i in range(len(nums))
#     if is_prime(i) and nums[i] % 2 != 0 and nums[i] > sum(nums)/len(nums)
# ]
    
# nums = [10, 7, 3, 12, 9, 5, 8, 11]

# print(f(nums))

#task 24
# def longest_increasing_sublist(nums):

#     longest = [nums[0]]
#     current = [nums[0]]

#     for i in range(1, len(nums)):

#         if nums[i] > nums[i-1]:
#             current += [nums[i]]

#         else:
#             if len(current) > len(longest):
#                 longest = current

#             current = [nums[i]]

#     if len(current) > len(longest):
#         longest = current

#     return longest

# print(longest_increasing_sublist([1,2,3,2,4,5,6,1]))

#task 25

# def my_sum(lst):
#     s = 0
#     for n in lst:
#         s += n
#     return s

# f = lambda nums: [
#     my_sum(sub)/len(sub)
#     for sub in nums
#     if len(sub) >= 3 and my_sum(sub) % 2 == 0
# ]

# nums = [
#     [1,2,3],
#     [4,5],
#     [6,7,8],
#     [1,1,1,1]
# ]
# print(f(nums))

#task 26
# def remove_duplicates_keep_last(nums):
    
#     result = []

#     for i in range(len(nums)):

#         duplicate = False

#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 duplicate = True
#                 break

#         if not duplicate:
#             result += [nums[i]]

#     return result

# print(remove_duplicates_keep_last([1,2,3,2,4,1]))


# TASK 27
# f = lambda w: sorted(w, key=lambda x: (-len(x), x))[:5]

# w = ["apple", "banana", "kiwi", "cherry", "date", "grape", "pear"]

# print(f(w))


# TASK 28
# def moving_average(nums, k):
#     result = []

#     for i in range(len(nums) - k + 1):
#         window = [i, i + k]

#         if any(n < 0 for n in window):
#             continue

#         avg = sum(window) / k
#         result.append(avg)
        
#     return result

# print(moving_average([1,2,3,-1,-2,3], 2))

# TASK 29
# func = lambda a, b: list(
#     filter(
#         lambda x: x not in b and x > sum(a) / len(a),
#         a
#     )
# )

# print(func([1,5,7,10], [5,3]))

# TASK 30
# def analyze_string_list(words):
#     result = []

#     for word in words:

#         has_digit = False
#         for ch in word:
#             if ch.isdigit():
#                 has_digit = True
#                 break

#         if has_digit:
#             continue

#         if word in result:
#             continue

#         if len(word) % 2 == 0:
#             result.append(word[::-1])
#         else:
#             result.append(word.upper())

#     return result

# words = ["hello", "cat", "dog2", "cat", "hi"]

# print(analyze_string_list(words))

###  DICT AND SET
# TASK 1
# def invert_unique(d):
#     result = {}

#     for key in d:
#         value = d[key]

#         if value not in result:
#             result[value] = [key]
#         else:
#             if key not in result[value]:
#                 result[value].append(key)

#     return result

# d = {
#     "a": 1,
#     "b": 2,
#     "c": 1,
#     "d": 3,
#     "e": 2
# }
# print(invert_unique(d))

# TASK 2
# func = lambda s: set(
#     filter(
#         lambda x: x > sum(s)/len(s) and x % 2 != 0 and x % 5 != 0,
#         s
#     )
# )

# print(func({1,3,5,7,9,11}))

# TASK 3
# def merge_dicts_sum(d1, d2):
#     result = {}

#     for key in d1:
#         result[key] = d1[key]

#     for key in d2:
#         if key in result:
#             result[key] += d2[key]
#         else:
#             result[key] = d2[key]

#     return result

# d1 = {"a": 5, "b": 3, "c": 7}
# d2 = {"b": 4, "c": 2, "d" : 10}
# print(merge_dicts_sum(d1, d2))

# TASK 4
# def filter_sets(sets_list):
#     result = []

#     for s in sets_list:

#         if len(s) <= 3:
#             continue

#         has_negative = False
#         has_even = False

#         for n in s:
#             if n < 0:
#                 has_negative = True
#             if n % 2 == 0:
#                 has_even = True

#         if not has_negative and has_even:
#             result.append(s)

#     return result

# sets_list = [
#     {1, 2, 3, 4},
#     {1, 3, 5},
#     {2, 4, 6, 8},
#     {1, -2, 3, 4},
#     {7, 9, 11, 13}
# ]

# print(filter_sets(sets_list))

# TASK 5
# func = lambda d: [
#     k for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0]))
# ][:5]

# d = {
#     "apple": 5,
#     "banana": 3,
#     "orange": 5,
#     "grape": 2,
#     "melon": 5,
#     "pear": 3
# }

# print(func(d))

# TASK 6
# def deep_sum(d):
#     total = 0

#     for value in d.values():

#         if type(value) == int or type(value) == float:
#             total += value

#         elif type(value) == list:
#             for num in value:
#                 total += num
        
#         elif type(value) == dict:
#             total += deep_sum(value)

#     return total

# data = {
#     "a": 5,
#     "b": [1,2,3],
#     "c": {"d": 4}
# }
# print(deep_sum(data))

# TASK 7
# def set_dw(A, B):
#     result = set()


#     for ch in A:
#         if ch not in B:
#             if ch % 2 == 0:
#                 result.add(ch)

#     for item in B:
#         if item not in A:
#             if item % 2 == 0:
#                 result.add(item)



#     return result


# print(set_dw({1, 2, 3, 4}, {4, 5, 6, 3}))

# TASK 7
# func = lambda A, B: {x for x in (A ^ B) if x % 2 == 0}

# print(func({1, 2, 3, 4}, {4, 5, 6, 3}))

# TASK 8 
# def sort_dict_by_value_length(d):
#     items = []

#     for key in d:
#         items.append((key, d[key]))

#     items.sort(key=lambda x: (len(x[1]), x[0]))

#     return items

# d = {
#     "apple": "red",
#     "banana": "yellow",
#     "kiwi": "green"
# }

# print(sort_dict_by_value_length(d))

# TASK 9
# def common_elements_all(sets_list):

#     if not sets_list:
#         return set()

#     result = set()

#     first_set = sets_list[0]

#     for element in first_set:
#         common = True

#         for s in sets_list:
#             if element not in s:
#                 common = False
#                 break

#         if common:
#             result.add(element)

#     return result


# sets_list = [
#     {1,2,3},
#     {2,3,4},
#     {0,2,3}
# ]
# print(common_elements_all(sets_list))

# TASK 10
# def filter_sort_dict(d):
#     result = {}

#     for key in d:
#         char = []

#         for num in d[key]:
#             if num % 2 != 0:
#                 char.append(num)

#         char.sort()

#         if len(char) > 0:
#             result[key] = char

#     return result

# data = {
#     "a": [1, 2, 3, 4],
#     "b": [2, 4, 6],
#     "c": [5, 3, 1],
#     "d": []
# }

# print(filter_sort_dict(data))

    