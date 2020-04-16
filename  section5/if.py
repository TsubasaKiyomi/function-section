
def if_egg(raw):
    if raw == "raw":
        print("生卵")
    elif raw == "boiled":
        print("茹で卵")
    elif raw == "soft_boiled":
        print("半熟卵")
    else:
        print("煮卵")


# qusetion「吾輩は＿＿＿である」
def if_question(qusetion):
    if qusetion == "猫":
        print("正解")
    elif qusetion == "ネコ":
        print("正解")
    elif qusetion == "ねこ":
        print("正解")
    elif qusetion == "cat":
        print("正解")
    else:
        print("不正解")


if_egg("raw")
# if_question()内に「吾輩は＿＿＿である」の答えを入れると正負が出力される
if_question("ねこ")
