def set_num(a):
    a = [1, 2, 3, 4, 5]
    b = a
    b[0] = 300
    return b
# 変数aに[]内の数字を入れ変数bに代入しbの0番目に
# 300を入れリターンでnum関数へ


get_num = set_num(1)
print(get_num)


def set_number(e):
    c = [5, 4, 3, 2, 1]
    e = c.copy()
    e[4] = "s"
    return e


num_num = set_number(1)
print(id(set_number(0)))
print(id(num_num))
# .copyしたのでid番号は違う
print(set_number(0))
print(num_num)
# id番号は違うが出力結果は同じになってしまう

# i = [1, 2, 3, 4, 5]
# j = i
# j[0] = 100
# print('j=', i)
# print('i=', i)


# x = [1, 2, 3, 4, 5]
# y = x.copy()
# y[0] = 100
# print('y =', y)
# print('x =', x)

# listx = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
# listr = listx
# listr[0] = "g"
# print(listr)
# print(listx)

# listd = [5, 4, 3, 2, 1]
# liste = listd.copy()
# liste[0] = 900
# print(listd)
# print(liste)
