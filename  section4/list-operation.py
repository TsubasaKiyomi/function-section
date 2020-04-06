def set_operation(a, b, c):
    return a + b + c


get_num = set_operation(["1", "2", "3", "4", "5", "2"],
                        ["asdfgh"], ["1989891"] + [34567])


numbers_x = [1, 2, 3, 4]
numbers_a = [5, 6, 7, 8]
numbers_x.extend(numbers_a)

print(numbers_x)  # aにbの値が入る
get_num.append(numbers_x)

print(get_num)  # sの値を最後尾に入れる

print(get_num[7])
get_num[0:4] = "hello"
print(get_num)  # 0~4番目をhello表示に変える

get_num[0:5] = []
print(get_num)
print(type(get_num[2]))

get_num.append(100)

print(get_num)  # 最後尾に追加

get_num.insert(1, "hello" + "323")

print(get_num)  # 指定した場所に挿入「文字」「数字」可

get_num.pop()

print(get_num)  # 最後尾の物を消す

get_num.pop(1)

print(get_num)  # （）で指定した場所を消す

del get_num[2]  # []で指定した場所を消す

print(get_num)  # del get_num get_numの中身全て消す
