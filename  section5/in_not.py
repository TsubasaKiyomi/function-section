# inとnot in
# # 返り値はないのでretrunはないif関数を使う


def in_or_not():
    # "a"に"b"の値があれば"in"と表示
    if list_number_b in list_number_a:
        print("in")
    # "a"に"b"の値がなければ"not in"と表示
    if 4 not in list_number_a:
        print("not in")


# not in を使用しているので a のリストに b の数字かなければ True 同じ数字があれば　False
def true_or_false():
    if number_list_b not in number_list_a:
        print(True)
    else:
        print(False)


list_number_a = [1, 2, 3]
list_number_b = 2
in_or_not()

number_list_a = [0, 1, 2]
number_list_b = 5
true_or_false()
