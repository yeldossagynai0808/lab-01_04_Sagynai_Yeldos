# def analyze_text(text):
#     text = text.lower()
#     vowels = "aeiou"

#     cleaned = ""
#     for ch in text:
#         if ch.isalpha():
#             cleaned += ch
#         else:
#             cleaned += " "

#     lst = []
#     word = ""

#     for ch in cleaned:
#         if ch != " ":
#             word += ch
#         else:
#             if word != "":
#                 lst += [word]
#                 word = ""

#     if word != "":
#         lst += [word]

#     vowel_set = set()
#     for ch in cleaned:
#         if ch in vowels:
#             vowel_set.add(ch)

#     new_words = []
#     seen = set()

#     for item in lst:
#         if len(item) >= 5 and item[0] == item[-1] and item not in seen:
#             new_words += [item]
#             seen.add(item)

#     return len(vowel_set), " ".join(new_words)

# print(analyze_text("Anna John qazaq radar level lambda text republic"))

# TASK 2
# def text_filter(text):
#     numbers = "1234567890"
#     cleaned = ""

#     for ch in text:
#         if ch not in numbers:
#             cleaned += ch

#     lst = cleaned.split()

#     result = []

#     for item in lst:
#         if len(item) % 2 == 0:
#             item = item[::-1]
#         result += [item]

#     return result

# print(text_filter("abc123 dragan qazaq Soul Good Man Breaking Bad"))

# TASK 3
# def top_k_words(text, k):
#     text = text.lower()
#     cleaned = ""

#     for ch in text:
#         if ch.isalpha() or ch == " ":
#             cleaned += ch
#         else:
#             cleaned += " "

#     words = cleaned.split()

#     freq = {}

#     for word in words:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1

#     items = list(freq.items())

#     for i in range(len(items)):
#         for j in range( i + 1, len(items)):

#             if items[j][1] > items[i][1] or (
#                 items[j][1] == items[i][1] and items[j][0] < items[i][0]
#             ):
#                items[i], items[j] = items[j], items[i]
        
#         result = []
#         for i in range(min(k, len(items))):
#             result.append(items[i][0])

#         return result

# print(top_k_words("apple banana apple orange banana apple kiwi orange banana", 2))
        

# TASK 4
# filter_words = lambda text: " ".join(
#     word.lower()
#     for word in text.split()
#     if sum(1 for c in word if c.isupper()) == 1
#     and not word[0].isupper()
#     and not word[-1].isupper()
# )
         
# print(filter_words("heLlo WorLd PyThon aBcD TesT"))

# TASK 5
# def compress_text(text):
#     if text == "":
#         return ""

#     result = ""
#     count = 1

#     for i in range(1, len(text)):
#         if text[i].lower() == text[i - 1].lower():
#             count += 1
#         else:
#             if count > 1:
#                 result += text [i - 1] + str(count)
#             else:
#                 result += text[i - 1]
#             count = 1
    
#     if count > 1:
#         result += text[-1] + str(count)
#     else:
#         result += text[-1]

#     return result

# compress_text("aaBBcDDD")

# TASK 6
# def len_word_4(text):
#     word = ""
#     lst = []

#     for w in text:
#         if w != " ":
#             word += w
#         else:
#             lst += [word]
#             word = ""

#     if word != "":
#         lst += word

#     new_lst = []

#     for char in lst:
#         if len(char) > 4:
#             new_lst += [char]

#     return new_lst

# print(len_word_4("Computer IT Preleminetry Test abc123"))


# nums = "1234567890"
# word = "Computer IT Preleminetry Test abc123"
# nw_word = word.split()

# func = lambda text: list(
#     filter(lambda x: len(x) >= 4 and x.isalpha() and len(set(x)) == len(x),
#     text.split()
#     )
# )

# print(func("Computer IT Test book apple abc123 lamp"))


def palindrome_words(text):
    cleaned = ""

    for ch in text:
        if ch.isalpha() or ch == " ":
            cleaned += ch

    words = []
    word = ""

    for ch in cleaned:
        if ch != " ":
            word += ch
        else:
            if word != "":
                words.append(word.lower())
                word = ""

    if word != "":
        words.append(word.lower())

    pal = []

    for w in words:
        if len(w) >= 3 and w == w[::-1]:
            if w not in pal:
                pal.append(w)

    for i in range(len(pal)):
        for j in range(i+1, len(pal)):

            if len(pal[j]) > len(pal[i]) or (
                len(pal[j]) == len(pal[i]) and pal[j] < pal[i]
            ):
                pal[i], pal[j] = pal[j], pal[i]

    return pal


