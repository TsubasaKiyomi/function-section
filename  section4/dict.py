def lists():
    # dict型を色々追加できる
    d = {"x": 10, "z": 30}
    d[1] = 100
    d["hello"] = "hello"
    # d = {"x": 50, "z": 200}
    # 元々あるもの"x""z"に新しく入れると上書きされる
    print(type(d))
    print(d)


lists()
