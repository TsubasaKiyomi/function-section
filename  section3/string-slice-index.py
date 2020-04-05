word = "hello world"

print(word[2])
print(word[6])


def greeting(a, b, c):
    s = a + b + c
    return s


num = greeting("おはようございます", '\nこんにちは', '\nこんばんわ')
print(len(num))
print(num[0:9])
print(num[10:15])
print(num[16:])
num = 'good', 'morning ' + num[16:]
print(num)
