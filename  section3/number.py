# mathの使い方
import math
x = 1.2345
print(math.floor(x))
# floor関数は浮動小数点の最大の整数を返す

x = 1.2345
print(math.ceil(x))
# ceil関数は浮動小数点の最小の整数を返す

# 10を5回かけた


def test(a, b):
    x = a**b
    return x


num = test(10, 5)
print(num)


def number(a, b):
    c = a*b
    return c


answer = number(10, 10)
print(answer)

# 17割る3の余り


def numb(a, b):
    c = a % b
    return c


ans = numb(17, 3)
print(ans)

# 割った際の小数点以下を切り捨て


def dnumb(a, b):
    c = a // b
    return c


ans = dnumb(17, 6)
print(ans)
