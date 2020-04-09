count = 0
# elseはbreakが無い場合などに使う。breakしなかったらループから抜ける。
while count < 5:
    print(count)
    count += 1
else:
    print("抜けます")

# breakがあればbreakでループから抜けるが、もしループから抜けなくても、elseでループから抜ける。
while count < 5:
    if count == 2:
        break
    print(count)
    count += 1
else:
    print("抜けます")
