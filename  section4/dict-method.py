def methods():
    m = {"x": 10, "z": 30}
    f = {"x": 300, "g": "hello"}
    m.update(f)  # 同じキーのものをアップデートできる
    print(m)
    print(m["x"])  # mのなかにある"z"キーから値を取れる
    m.pop("x")  # mのなかにある"x"を消せる
    del m["z"]  # mのなかにある"z"キーを消せる
    print(m)
    m.clear()  # mの中身を消す
    print(m)
    print("g" in f)  # "g"キーはfの中にあるか？


methods()


def scre():
    math = {"田中": 85, "鈴木": 76, "木下": 90}
    science = {"田中": 65, "鈴木": 87, "木下": 70}
    english = {"田中": 75, "鈴木": 57, "木下": 78}
    print(math)
    print(science)
    print(english)
    print(math["田中"], science["田中"], english["田中"])
    print(math["鈴木"], science["鈴木"], english["鈴木"])
    print(math["木下"], science["木下"], english["木下"])
    print(m)


scre()
