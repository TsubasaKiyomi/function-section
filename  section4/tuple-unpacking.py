# タプルのアンパッキング
def multiplication(*n):
    return n


answer = multiplication(1, 2, 3)


def name(a, b):
    a, b = b, a  # "山田""太郎"を"太郎"山田"にする
    farst = a, b
    return farst


family_name = name("山田", "太郎")


tuple_fruits = "banana", "orange", "apple"
a, b, c = tuple_fruits


print(a)
print(b)
print(c)
print("#####################")
a, b, c = b, c, a  # 中身を入れ替える
print(a)
print(b)
print(c)

print(answer)
print(type(answer))

print(family_name)
print(type(family_name))
