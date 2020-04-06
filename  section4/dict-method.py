def dict_methods():
    kyes_a = {"x": 10, "z": 30}
    kyes_b = {"x": 300, "g": "hello"}
    kyes_a.update(kyes_b)  # 同じキーのものをアップデートできる
    print(kyes_a)
    print(kyes_a["x"])  # kyes_aのなかにある"z"キーから値を取れる

    kyes_a.pop("x")  # kyes_aのなかにある"x"を消せる

    del kyes_a["z"]  # kyes_aのなかにある"z"キーを消せる
    print(kyes_a)

    kyes_a.clear()  # kyes_aの中身を消す

    print(kyes_a)
    print("g" in kyes_b)  # "g"キーはfの中にあるか？


dict_methods()


def scres_list():
    math = {"田中": 85, "鈴木": 76, "木下": 90}
    science = {"田中": 65, "鈴木": 87, "木下": 70}
    english = {"田中": 75, "鈴木": 57, "木下": 78}

    print(math)
    print(science)
    print(english)
    print(math["田中"], science["田中"], english["田中"])
    print(math["鈴木"], science["鈴木"], english["鈴木"])
    print(math["木下"], science["木下"], english["木下"])


scres_list()
