def even_odd(number):
    if number % 2 == 0:
        return "偶数です"
    return "奇数です"


for i in range(1, 11):
    print(str(i) + "=" + even_odd(i))


def a_than(choose_numbers):
    if choose_numbers != 4:
        return("ok")
    return("bad")


print(a_than(2))
