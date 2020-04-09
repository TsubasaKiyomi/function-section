# コメントはコードの上に記載する。（pythonの暗黙の了解）


def furits_lisst(*a):
    return a


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

# print(good_time_to_eat)


def furits_japanes_name(*a):
    a


# 改行は「\n」　行が長くなる場合は 「\ + 改行」
furits_eat = "バナナ, オレンジ, りんご, " \
    + "イチゴ\nパイナップル, みかん, " \
    + "さくらんぼ\nスイカ, メロン, 梨, 桃"
print(furits_eat)


for i in range(1):
    print("banana""\n改行されます")
    furits_name = "さくらんぼ　パイナップル　スイカ　梨　桃　メロン" \
        + "一行になります" "りんご　バナナ　みかん　イチゴ　ドライフルーツ ブルーベリー"
    print(furits_name)
