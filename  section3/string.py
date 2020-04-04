def greeting(a, b, c):
    s = a + b + c
    return s


num = greeting("Hello python", '\nMi name is Mike', '\nHow are you?')
print(num)


def name(a, b, c, d):
    e = a+b+c+d
    return e


farst = name("suszuki", "\ntanaka", "\nkobayashi", "\nsasaki")
print(farst)


def mod(coin):
    if coin == '表':
        return('赤組')
    elif coin == '裏':
        return('白組')
    else:
        return('どちらでもない')


onamae = mod('表')
print(onamae)
