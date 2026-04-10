# func = lambda x: "положительно" if x > 0 else "ноль" if x == 0 else "отрицательно"

# print(func(5))
# print(func(-3))
# print(func(0))


# numbers = [5,12,7,20,33,8]

# func = list(filter(lambda n: n > 0 and n % 2 == 0, numbers))

# print(func)

# generator
# task 3
def infinite_numbers():
    for i in range(1, 20):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 3 == 0:
            yield "Fizz"
        else:
            yield i

print(infinite_numbers())

#comprehension
#task 3
# words = ["кот", "машина", "ананас", "дом"]

# lst = [ w for w in words if len(w)> 4 and "а" in w]

# print(lst)

#task generator + map + filter + if

# def process_numbers(numbers):
#     posstive = list(filter(lambda n: n > 0, numbers  ))

#     func = ( p/2 if p % 2 == 0 else p*3+1 for p in posstive)
#     return func

# numbers = [5, -2, 8, 0, -7, 3]
# for x in process_numbers(numbers):
#     print(x)

#task filter

# numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]

# evens = list(filter(lambda x: x % 2 == 0, numbers))

# print(evens)


