def raed_namber(a):
    return a


number_x = raed_namber([1, 1, 2, 2, 3, 3, 4, 5, 1, 2, 3])


def get_list(b):
    return b


number_z = get_list("Mi name is ボブ.")
to_split = number_z.split(" ")  # .splitはリストに入れてスペースで分ける
number_s = " ".join(to_split)  # .joinはリストのデータを空白文字で繋げる


def get_nam(**a):
    s = a
    return s


set_suitable_list = ["abcdeabcde", " ssddxx", " ffddeerr"]
set_suitable_list.reverse()  # 順番を逆にする


print(set_suitable_list)
set_suitable_list.sort(reverse=True)

print(set_suitable_list)
set_suitable_list.sort()

print(set_suitable_list)
print(number_x.index(3, 6))  # 6番目以降の３の場所
number_x.reverse()  # 順番を逆にする
print(number_x)

number_x.sort()  # 数字の小さい順に並び替える
print(number_x)

number_x.sort(reverse=True)  # 数字の大きい順に並び替え x.reverse()でも可能
print(number_x)
print(number_s.title())  # .titleで頭文字だけ大きくする
print(to_split)
