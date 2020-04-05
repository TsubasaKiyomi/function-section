def set_tuple(a):
    d = a
    return d


t = set_tuple((1))
print(type(t))
# ()をつつけても(,)がないのでint型になる

x = set_tuple(1,)
print(type(x))
# (,)をつけても()がないのでint型になる

s = set_tuple((1,))
print(type(s))
# ()も(,)もついているのでtuple型になる

g = set_tuple((2,))
f = set_tuple((4,))
print(g+f)
# (2,4)

# g = set_tuple((2,))
# f = set_tuple((4))
# print(g+f)
# 型が違うのでエラー
