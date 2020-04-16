# iでインデックス番号と変数fruitに入れた物を同時に表示させたい時i = 0、i += 1でカウントしていく
def fruit():
    i = 0
    for fruit in ["apple", "banana", "orange"]:
        print(i, fruit)
        i += 1


# enumerate()関数を使用して上記より簡単に表現する。
# インデックス番号、要素の順番で取得できる。
def fruits():
    for i, fruit in enumerate(["apple", "banana", "orange"]):
        print(i, fruit)


def festival_sweets():
    for i, sweets in enumerate(["チョコバナナ", "りんご飴", "綿あめ"]):
        # インデックス数を変更するにはprint()内で + 1とするfor文内でするとエラーになる。
        print(i + 1, sweets)


fruit()
fruits()
festival_sweets()
