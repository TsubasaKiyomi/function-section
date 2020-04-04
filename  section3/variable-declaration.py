# 変数宣言、print関数使い方


def num():
    print('hello', type('hello'), end='.\n')
    # end=.\n「.」をつけ「\n」で改行
    print(10, type, '10', type(10), sep=',')
    # sep:セパレーション「,」で区切る
    print(2.0, type(2.0))


num()

