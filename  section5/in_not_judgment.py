# list_numberに何も入れながった場合は”False”になる。何か値が入れば”Ture”
# Falseになる値　0, 0.0, " ", [], (), {}, set()
list_number = 0


def judgment():
    if list_number:
        print("Ok")
    else:
        print("NO")


judgment()


test_list = ["put_here"]


def test():
    if test_list:
        print(True)
    else:
        print(False)


test()
