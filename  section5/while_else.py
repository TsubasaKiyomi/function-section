elses = 0


def loops(elses):
    elses


# elseはbreakが無い場合などに使う。breakしなかったらループから抜ける。
while elses < 5:
    print(elses)
    elses += 1
else:
    print("抜けます")


loops("elses")

count = 0


def loop_count(count):
    count


# breakがあればbreakでループから抜けるが、もしループから抜けなくても、elseでループから抜ける。
while count < 5:
    if count == 2:
        break
    print(count)
    count += 1
else:
    print("抜けます")


loop_count("count")
