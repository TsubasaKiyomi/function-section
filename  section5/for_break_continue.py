def number_even():
    for even in range(1, 11):
        # range()の内の数字が[ % 2 == 2:] 2で割り切れるのなら"偶数"
        if even % 2 == 0:
            print("偶数", even)
        continue
    else:
        print("終わり")


number_even()


def number_odd():
    for odd in range(1, 11):
        # range()の内の数字が[ % 3 == 3:] 3で割り切れるのなら"奇数"
        if odd % 3 == 0:
            print("奇数", odd)
        continue
    else:
        print("終わり")


number_odd()


def words():
    for word in ["表示されます１", "ここはスキップされます", "表示されます２", "表示されます３"]:
        if word == "ここはスキップされます":
            continue
        print(word)


words()


def num_loop():
    for i in [1, 2, 3, 4]:
        if i == 3:
            print("3回目です。ループを抜けます")
        break
    print(str(i) + "回目です。3回目のループを抜けます")


num_loop()
