def greeting_words(a, b, c):
    return a + b + c


def family_name(a, b, c, d):
    return a + b + c + d


def which_coins(coin):
    if coin == '表':
        return('赤組')
    elif coin == '裏':
        return('白組')
    else:
        return('どちらでもない')


print(greeting_words("Hello python", '\nMi name is Mike', '\nHow are you?'))
print(family_name("suszuki", "\ntanaka", "\nkobayashi", "\nsasaki"))
print(which_coins('裏'))
