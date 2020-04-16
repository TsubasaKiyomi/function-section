# print(kwargs) kwargsは辞書型
def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


# menu(entree="beef", drink="coffee")
# menu(**kwargs)に d = {}の中身が展開されて渡され、さらに辞書化されfro文のファンクション内で辞書として扱われる。
d = {"entree": "beef", "drink": "ice coffee", "dessert": "ice"}


def menu1(food, *args, **kwargs):
    # foodには"banana"が位置引数出力される #banana
    print(food)
    # argsには *argsの複数個の引数が出力される　「タプル化」されたものが出力される！ #('apple', 'orange')
    print(args)
    # キーワード引数として渡したものが（entree="beef",drink="coffee"）が
    # **kwargsに入り出力「辞書化」された物が出力される！ #{'entree': 'beef', 'drink': 'coffee'}
    print(kwargs)


def name(*args):
    # argsの場合はタプルで出力される
    print(args)
    # *argsの場合はstrで出力される！
    print(*args)


def prefecture_name(**kwargs):
    #　辞書型でキーワードとバリューのどちらも出力される
    print(kwargs)
    #　strでキーワードのみ出力される
    print(*kwargs)
    # エラーとなる
    # print(**kwargs)


menu(**d)
name("sasaki", "ueda", "kobayasihi", "sato")
menu1("banana", "apple", "orange", entree="beef", drink="coffee")
prefecture_name(
    Tochigi="Utsunomiya",
    Saitama="Saitamacity",
    Kanagawa="Yokohamacity",
    Chiba="Chibacity")
