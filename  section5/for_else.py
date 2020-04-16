def gass(gasoline):
    # ガソリンを満タンまで入れる。range()関数で1〜5回の間でループさせる。
    for gasoline in range(1, 5):
        if gasoline <= 3:
            print(str(gasoline * 10) + "リッター入りました。")
            print("まだ満タンではないです。")
        if gasoline == 4:
            # str()で「i」の回数*書ける10で10倍の値をだし、リッター数とした。
            print(str(gasoline * 10) + "リッター入りました。")
            print("間も無く満タンです・・・")
# breakが無いのでelseでループを抜ける。最後は満タンを表示する。
    else:
        print("満タンになりました！")


def treasure_empty(treasure_box):
    for treasure_box in ["空っぽ", "空っぽ", "空っぽ", "宝箱", "空っぽ"]:
        if treasure_box == "宝箱":
            print("宝箱です！！")
        if treasure_box == "空っぽ":
            print("空っぽでした。")
    else:
        print("もうありません。")


gass("gasoline")
treasure_empty("treasure_box")
