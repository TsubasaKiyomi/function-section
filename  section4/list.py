def list_orchid(a, b, c):
    return a + b + c


list_num = list_orchid(["012345"], ["6789"], [1234567890])


print(list_num[::-1])
print(len(list_num[0]))
print(list_num[0][1])  # [0]と[1]は”　”で囲ったのでstr型。出力結果を求められる。
print(list_num[1][3])  # [2]のint型から出力結果を求めるとタイプエラーになる
print(type(list_num[1]))
print(type(list_num[2]))
