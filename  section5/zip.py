# forループの中でイテラブルオブジェクトの要素を同時に取得して使う場合はzip()関数を使用する。

# zipを使用せずに書くとprint()に[i]を３回も書かなければならない。
# def nozip():
#     days = ["mon", "Tue", "wed"]
#     fruits = ["appole", "banana", "oraneg"]
#     dorinks = ["coffee", "tea", "beer"]

#     for i in range(len(days)):
#         print(days[i], fruits[i], dorinks[i])


# nozip()


# zip関数を使用して上記より簡単にする。
def zips():
    days = ["mon", "Tue", "wed"]
    fruits = ["appole", "banana", "oraneg"]
    drinks = ["coffee", "tea", "beer"]

    for day, fruit, drink in zip(days, fruits, drinks):
        print(day, fruit, drink)


def curry():
    spicy = ["sweet", "medium_spicy", "spicy"]
    drinks = ["tea", "water", "lassie"]
    days = ["mon", "Tue", "wed"]

    for spice, drink, day in zip(spicy, drinks, days):
        print(spice, drink, day)


zips()
curry()
