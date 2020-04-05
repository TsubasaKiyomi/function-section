def set_operation(a, b, c):
    x = a+b+c
    return x


get_num = set_operation(["1", "2", "3", "4", "5", "2"],
                        ["asdfgh"], ["1989891"] + [34567])


s = [1, 2, 3, 4]
a = [5, 6, 7, 8]
s.extend(a)
# sにaの値が入る
print(s)
get_num.append(s)
# sの値を最後尾に入れる
print(get_num)

print(get_num[7])
get_num[0:4] = "hello"
# 0~4番目をhello表示に変える
print(get_num)

get_num[0:5] = []
print(get_num)
print(type(get_num[2]))

get_num.append(100)
# w最後尾に追加
print(get_num)

get_num.insert(1, "hello"+"323")
# 指定した場所に挿入「文字」「数字」可
print(get_num)

get_num.pop()
# 最後尾の物を消す
print(get_num)

get_num.pop(1)
# （）で指定した場所を消す
print(get_num)

del get_num[2]
# []で指定した場所を消す
print(get_num)

# del get_num get_numの中身全て消す
