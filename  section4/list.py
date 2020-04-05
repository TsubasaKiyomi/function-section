def list(a, b, c):
    d = a+b+c
    return d


list_num = list([12345], [678910], [1234567890])
list_num = list(["abcdef"], [678910], [1234567890])
list_num = list(["abcdef"], ["ghijk"], [1234567890])
list_num = list(["012345"], ["6789"], [1234567890])

#
# print(list_num)
print(list_num[:])
# print(list_num[::-1])
print(len(list_num[0]))
print(list_num[0][2])  # [0]と[1]は”　”で囲ったのでstr型。出力結果を求められる。
print(list_num[1][3])  # [2]のint型から出力結果を求めるとタイプエラーになる
print(type(list_num[1]))
print(type(list_num[2]))
