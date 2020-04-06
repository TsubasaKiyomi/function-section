def set_num_list(a):
    a = [1, 2, 3, 4, 5]
    b = a
    b[0] = 300
    return b


# 変数aに[]内の数字を入れ変数bに代入しbの0番目に300を入れリターンでnum関数へ
get_number = set_num_list(1)


def copy_number(e):
    c = [5, 4, 3, 2, 1]
    e = c.copy()
    e[4] = "s"
    return e


num_num = copy_number(1)


print(get_number)
print(id(copy_number(0)))
print(id(num_num))  # .copyしたのでid番号は違う
print(copy_number(0))
print(num_num)  # id番号は違うが出力結果は同じになってしまう
