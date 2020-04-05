# 変数宣言、print関数使い方
# 変数にデータを入れ、宣言する

num = 1
print(num)
print(type(num))
num = "1"
print(num)
print(type(num))
num = 1.2
print(num)
print(type(num))


def each_variable():
    print('hello\n', type('hello'), end='.\n')
    # end=.\n「.」をつけ「\n」で改行
    print(10, type('10'), type(10), sep=',')
    # sep:セパレーション「,」で区切る
    print(2.0, type(2.0))


each_variable()
