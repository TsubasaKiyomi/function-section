# set集合型のmethodメソッド


def set(a):
    a


a = {1, 2, 3, 4}
a.add(5)
a.add(10)
a.add("apple")
#  #同じ(" ")ないには２つ入れられない。１つだけ。
# a.add("test", "hello")
print(a)

# {1, 2, 3, 4, 5, 10, 'apple'}の指定した()内を消す
a.remove(2)
print(a)

# ()内を全て消す
a.clear()
print(a)

a = {1, 2, 3}
b = {3, 4, 5}


# 和集合の計算
# |(パイプ)か.unionで重複した３を１つにして出力
c = b | a
print(c)
c = b.union(a)
print(c)

# aとbどちらにもある数字
c = a & b
print(c)
c = a.intersection(b)
print(c)

# aからbを引いた値
c = a - b
print(c)
c = a.difference(b)
print(c)

# a,bの重複していない値
c = a ^ b
print(c)
c = a.symmetric_difference(b)
print(c)
