# dict辞書型をforループで処理する
def num():
    d = {"x": 100, "y": 200}
# この場合キーkyeの部分しかprint出力できない。
    for a in d:
        print(a)


num()


def for_value():
    c = {"x": 100, "y": 200}
# .itemsを使用することでキーkyeとバリューvalueを出力できる。
    for a, b in c.items():
        print(a, "/", b)
# c.itemsの中はdict_items([('x', 100), ('y', 200)])になっている。
# リストの中にタプル表記されておりキーとバリューが入っている。c.items()にリストの('x', 100)が入り
# タプルにでアンパッキングになっているので('x', 100)の'x'が変数aに100が変数bが入る。
        print(c.items())


for_value()


def size():
    size_men = {"S": 100, "M": 120, "L": 150, "LL": 180}
    for x, y in size_men.items():
        print(x, ":", y)


size()
