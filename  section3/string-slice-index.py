word = "hello world"

print(word[2])
print(word[6])


def greeting(a, b, c):
    s = a + b + c
    return s


get_greeting = greeting("おはようございます", '\nこんにちは', '\nこんばんわ')
print(len(get_greeting))
print(get_greeting[0:9])
print(get_greeting[10:15])
print(get_greeting[16:])
get_greeting = 'good', 'morning ' + get_greeting[16:]
print(get_greeting)
