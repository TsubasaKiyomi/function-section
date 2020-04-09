# ガチャのような物　回数を決めてループさせる。
count = 0
while True:
    if count == 1:
        count += 1
        print("レア")
        print("これで" + str(count) + "回目です。")

    if count == 2:
        count += 1
        print("スーパーレア")
        print("これで" + str(count) + "回目です。")

    if count == 3:
        count += 1
        print("ノーマル")
        print("これで" + str(count) + "回目です。")

    if count == 4:
        count += 1
        print("ノーマル")
        print("スキップします")
        continue

    if count == 5:
        count = 0
        # print("ノーマル")
        print("5回目はスキップされました。\n終わります。")
        break

    count += 1
    print("最初の" + str(count) + "回目です。")
