def get_greeting(a, b, c):
    s = a + b + c
    return s


set_greeting = get_greeting(
    "Hello python", '\nMi name is Mike', '\nHow are you?')

print(set_greeting)


def set_name(a, b, c, d):
    e = a+b+c+d
    return e


family_name = set_name("suszuki", "\ntanaka", "\nkobayashi", "\nsasaki")
print(family_name)


def set_coins(coin):
    if coin == '表':
        return('赤組')
    elif coin == '裏':
        return('白組')
    else:
        return('どちらでもない')


get_which = set_coins('裏')
print(get_which)
