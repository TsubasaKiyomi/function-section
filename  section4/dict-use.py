# dictの使い所
# リストと違いd辞書型はkyeがわかれば即座に値：valueが出力できる。


# fruits = {
#     "apple": 100,
#     "banana": 200,
#     "orange": 300,
# }

# print(fruits["apple"])

import random


# furits_item{} の中からランダムにkeyとvalを出す。
def furits(a):
    return a


furits_item = {
    'banana': '1',
    'apple': '3',
    'orange': '2',
    'coconut': '3',
    'grape': '2'
}
fruit, val = random.choice(list(furits_item.items()))
print(fruit, val)


# keys[]のkeyに対して(1〜10)の個数のvalを与える
keys = ["apple", "banana", "orange"]
quantity = {value: random.randint(1, 10)for value in keys}


print(quantity)
