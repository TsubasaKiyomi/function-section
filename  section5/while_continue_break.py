# ガチャのような物　回数を決めてループさせる。
count = 0


def loop(count):
    count


while True:
    count += 1
    if count == 1:
        print(str(count) + "回目です。何が出るかな？")
        print("レア")

    count += 1
    if count == 2:
        print(str(count) + "回目です。何が出るかな？")
        print("スーパーレア")

    count += 1
    if count == 3:
        print(str(count) + "回目です。何が出るかな？")
        print("ノーマル")

    count += 1
    if count == 4:
        print(str(count) + "回目です。5回目はスキップして終了します。")
        print("ノーマル")
        continue

    count = 5
    if count == 5:
        # print("ノーマル")
        print("5回目なので\n終わります。")
        break


loop("count")
