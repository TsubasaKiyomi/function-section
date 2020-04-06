word = "hello world"


def greeting(a, b, c):
    return a + b + c


get_greeting = greeting("おはようございます", '\nこんにちは', '\nこんばんわ')


print(word[2])
print(word[6])
print(len(get_greeting))
print(get_greeting[:9])
print(get_greeting[10:15])
print(get_greeting[16:])
get_greeting = 'good', 'morning ' + get_greeting[16:]
print(get_greeting)
