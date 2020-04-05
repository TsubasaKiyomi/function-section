def operation(a, b, c):
    x = a+b+c
    return x


num = operation(["1", "2", "3", "4", "5", "2"],
                ["asdfgh"], ["1989891"] + [34567])


s = [1, 2, 3, 4]
a = [5, 6, 7, 8]
s.extend(a)
# sにaの値が入る
print(s)
num.append(s)
# sの値を最後尾に入れる
print(num)

print(num[7])
num[0:4] = "hello"
# 0~4番目をhello表示に変える
print(num)

num[0:5] = []
print(num)
print(type(num[2]))

num.append(100)
# w最後尾に追加
print(num)

num.insert(1, "hello"+"323")
# 指定した場所に挿入「文字」「数字」可
print(num)

num.pop()
# 最後尾の物を消す
print(num)

num.pop(1)
# （）で指定した場所を消す
print(num)

del num[2]
# []で指定した場所を消す
print(num)

# del num numの中身全て消す
