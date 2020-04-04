def raed(a):
    s = a
    return s


x = raed([1, 1, 2, 2, 3, 3, 4, 5, 1, 2, 3])
print(x.index(3, 6))  # 6番目以降の３の場所
x.sort()  # 数字の小さい順に並び替える
print(x)
x.sort(reverse=True)  # 数字の大きい順に並び替え x.reverse()でも可能
print(x)
x.reverse()  # 順番を逆にする
print(x)


def test(b):
    c = b
    return c


z = test("Mi name is ボブ.")
to_split = z.split(" ")  # .splitはリストに入れてスペースで分ける
print(to_split)

s = " ".join(to_split)  # .joinはリストのデータを空白文字で繋げる
print(s.title())  # .titleで頭文字だけ大きくする


def ra(**a):
    s = a
    return s


# x = ra("abcdeabcde" "ssddxx" "ffddeerr")
# print(x.index("b", 3))  # 6番目以降の３の場所
x = ["abcdeabcde", " ssddxx", " ffddeerr"]
x.reverse()  # 順番を逆にする
print(x)
x.sort(reverse=True)
print(x)
x.sort()
print(x)
