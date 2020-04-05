def sub(a):
    d = a
    return d


t = sub((1))
print(type(t))
# ()をつつけても(,)がないのでint型になる

x = sub(1,)
print(type(x))
# (,)をつけても()がないのでint型になる

s = sub((1,))
print(type(s))
# ()も(,)もついているのでtuple型になる

g = sub((2,))
f = sub((4,))
print(g+f)
#(2,4)

g = sub((2,))
f = sub((4))
print(g+f)
#型が違うのでエラー
