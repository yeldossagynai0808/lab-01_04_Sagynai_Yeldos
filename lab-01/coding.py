import turtle

turtle.title("rainbow!")
turtle.speed(15)
turtle.bgcolor("black")
r,g,b=(255,0,0)

for i in range(255*2):
    turtle.colormode(255)
    if i < 255//3:
        g += 3
    elif i < 255*2//3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255*4//3:
        g -=3
    elif i < 255*5//3:
        r+= 3
    else:
        b-=3

        turtle.fd(50+i)
        turtle.rt(91)
        turtle.pencolor(r,g,b)

turtle.done()
#split()
# def my_split(text):
#     words = []
#     word = ""
#     for char in text:
#         if char != " ":
#             word += char
#         else:
#             if word != "":
#                 words.append(word)
#                 word = ""

#     if word != "":
#         words.append(word)
#     return words

# print(my_split("Hello world test"))
#.lower()
# def custom_lower(text):
#     lowercased = ""
#     for char in text:
#         if 'A'<= char <= 'Z':
#             lowercased += chr(ord(char) +32)
#         else:
#             lowercased += char
#     return lowercased

# print(custom_lower("Joelll"))


            