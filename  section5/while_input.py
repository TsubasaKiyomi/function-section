# input関数はキーボードに入力したデータを受け付けるための関数。
# input関数は標準入力として用意されている。


def test_command(word):
    word


while True:
    word = input("100と入力してみてください。:")
    num = int(word)
    if num == 100:
        break
    print("next")
test_command("word")


def lemon(color):
    color


while True:
    color = input("レモンは何色？")
    if color == "黄色":
        break
    elif color == "きいろ":
        break
    elif color == "yellow":
        break
    print(color)

lemon("color")


def idioms(idiom):
    idiom


while True:
    idiom = input("\n\n次の四字熟語を答えよ\n\n「１人で千人の敵をなぎ倒せるほど強い人。人並み外れた能力や経験があること。」:")
    if idiom == "一騎当千":
        break
print("「 {0} 」 正解です！！".format(idiom))


idioms("idiom")


# def be(bane):
#     bane
# min_length = 3
# name = input("4文字以上入力して:")
# while not(len(name) > min_length and name.isalpha()):
#     bane = input("4文字以上入力して:")
# print("あなたは, {0}と入力した".format(name))
# be("bane")
