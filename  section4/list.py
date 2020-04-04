def list(a, b, c):
    d = a+b+c
    return d


listnum = list([12345], [678910], [1234567890])
listnum = list(["abcdef"], [678910], [1234567890])
listnum = list(["abcdef"], ["ghijk"], [1234567890])
listnum = list(["012345"], ["6789"], [1234567890])

#
# print(listnum)
print(listnum[:])
# print(listnum[::-1])
print(len(listnum[0]))
print(listnum[0][2])#[0]と[1]は”　”で囲ったのでstr型。出力結果を求められる。
print(listnum[1][3])#[2]のint型から出力結果を求めるとタイプエラーになる
print(type(listnum[1]))
print(type(listnum[2]))
