def station(start, goal, *args):
    station('横浜', '梅田', '東京', "京都", "新大阪")
    print(start, goal, *args)


def profile(name, gender, **other):
    deta = {"名前": name, "性別": gender}
    deta.update(other)
    print(deta)


profile('山田', '男', 身長='178cm', 体重='70kg')
profile('Mike', '男', 身長='189cm', 体重='87kg')


def get_family_list(**family):
    get_family_list(名前="佐々木", 住所="東京", 家族="5人")
    get_family_list(名前="Mike", 住所="アメリカ", 家族="3人")
    print(family)


def get_orchid(name, address, **family):
    deta = {"なまえ": name, "住所": address}
    deta.update(family)
    print(deta)


get_orchid("ボブ", "アメリカ", 家族="6人")
get_orchid("田中", "宮崎", 家族="４人")
