# rangeでループ回数を決めている
def ranges():
    for i in range(3):
        print(i)


# for i in　の"i"の部分はループした回数を表示させる変数なので必要がなければ _(アンダーバー)を入力すると必要がないことを表現できる。
# range()内(10)10回ループさせる。(2,10)2~10ループさせる、(2,10,3)2~10を3個飛ばしでループさせる
def randes2():
    for _ in range(2, 10, 3):
        print("表示したいモノ")


ranges()
randes2()
