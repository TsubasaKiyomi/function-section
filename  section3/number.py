# mathの使い方
import math


# floor関数は浮動小数点の最大の整数を返す
print(math.floor(1.2345))


# ceil関数は浮動小数点の最小の整数を返す
print(math.ceil(1.2345))


# aをb回かける関数
def powar(a, b):
    return a**b


# a描けるbを計算する関数
def multiplication(a, b):
    return a * b


# a割るbの余りを計算する関数
def remainder(a, b):
    return a % b


# 割った際の小数点以下を切り捨てを計算する関数
def division_truncation(a, b):
    return a // b


print(powar(10, 5))
print(multiplication(10, 10))
print(remainder(17, 3))
print(division_truncation(17, 6))
