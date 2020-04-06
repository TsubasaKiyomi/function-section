def set_tuple(a):
    return a


# ()をつつけても(,)がないのでint型になる
tuple_b = set_tuple(1)
print(tuple_b)
print(type(tuple_b))


# (,)をつけても()がないのでint型になる
tuple_x = set_tuple(1,)
print(type(tuple_x))


# ()も(,)もついているのでtuple型になる
tuple_s = set_tuple((1,))
print(type(tuple_s))


# (2,4)繋げることができる
tuple_z = set_tuple((2,))
tuple_y = set_tuple((4,))
print(tuple_z + tuple_y)

# g = set_tuple((2,))
# f = set_tuple((4))
# print(g+f)
# 型が違うのでエラー
