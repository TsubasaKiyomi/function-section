empty = None


def True_or_False():
    if empty is not None:
        print("NONE!")
# (1 == True)は「真」同士なのでprint()表示すると「(1)」にまとめられてしまう。
# 「値」が"真"同士なのでTrueが返ってくる
    print(1)
    print(True == 1)
# [is]を使うと「値」が真同士でも、オブジェクト自体が異なるためFalseとなる
# オブジェクト同士が真でないとTrueにならない。
    print(1 is True)
    print(1 == False)
    print(1 is False)
# オブジェクト同士が一致しているのでTrue
    print(True is True)
    print(False is False)


True_or_False()
