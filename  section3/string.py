def get_greeting(a, b, c):
    return a + b + c


def set_name(a, b, c, d):
    return a + b + c + d


def get_coins(coin):
    if coin == '表':
        return('赤組')
    elif coin == '裏':
        return('白組')
    else:
        return('どちらでもない')


print(get_greeting("Hello python", '\nMi name is Mike', '\nHow are you?'))
print(set_name("suszuki", "\ntanaka", "\nkobayashi", "\nsasaki"))
print(get_coins('裏'))
