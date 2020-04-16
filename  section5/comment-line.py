# コメントはコードの上に記載する。（pythonの暗黙の了解）
def furits_lisst(*kwags):
    return kwags


good_time_to_eat = furits_lisst(
    "banana",
    "orangi",
    "apple",
    "Strawberry",
    "pineapple",
    "mandarin_orang",
    "cherry",
    "watermelon",
    "melon",
    "pear",
    "peach")


def furits_japanes_name(*entry_furits):
    return entry_furits


# 改行は「\n」　行が長くなる場合は 「\ + 改行」
furits_eat = furits_japanes_name("バナナ, オレンジ, りんご, "
                                 + "イチゴ\nパイナップル, みかん, "
                                 + "さくらんぼ\nスイカ, メロン, 梨, 桃")


def loop(loop_furits_name):
    for loop_furits_name in range(1):
        print("banana""\n改行されます")
        # \ + で結合して一行に表示できる。
        furits_name = "さくらんぼ　パイナップル　スイカ　梨　桃　メロン" \
            + "一行になります" "りんご　バナナ　みかん　イチゴ　ドライフルーツ ブルーベリー"
        print(furits_name)


print(good_time_to_eat)
print(furits_eat)
loop("loop_furits_name")
