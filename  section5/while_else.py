# elseはbreakが無い場合などに使う。breakしなかったらループから抜ける。
i = 0


def loops(i):
    print(loops)


while i < 2:
    print(i)
    i += 1
else:
    print(i)
    print("抜けます")
loops("i")


count = 0


def loop_count(count):
    return count


# breakがあればbreakでループから抜けるが、もしループから抜けなくても、elseでループから抜ける。
while count < 5:
    if count == 2:
        break
    print(count)
    count += 1
else:
    print("抜けます")


loop_count("count")
