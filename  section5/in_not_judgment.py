# list_numberに何も入れながった場合は”False”になる。何か値が入れば”Ture”
# Falseになる値　0, 0.0, " ", [], (), {}, set()


def judgment():
    if list_number:
        print("Ok")
    else:
        print("NO")


def True_or_false():
    if input_orchid:
        print(True)
    else:
        print(False)


list_number = 0
judgment()

input_orchid = ["ここに何か入力してください。入力するとTrueとなります"]
True_or_false()
