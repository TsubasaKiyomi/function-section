# mathの使い方

import math
x = 1.2345
print(math.floor(x))
# floor関数は浮動小数点の最大の整数を返す


x = 1.2345
print(math.ceil(x))
# ceil関数は浮動小数点の最小の整数を返す


def test(a, b):
    x = a**b
    return x


num = test(10, 5)
print(num)
# 10を5回かけた


def number(a, b):
    c = a*b
    return c


answer = number(10, 10)
print(answer)


def test_number(a, b):
    c = a % b
    return c


get_answer = test_number(17, 3)
print(get_answer)
# 17割る3の余り


def set_num(a, b):
    c = a // b
    return c


get_num = set_num(17, 6)
print(get_num)
# 割った際の小数点以下を切り捨て
