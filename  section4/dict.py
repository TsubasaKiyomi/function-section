def set_dict():
    # dict型を色々追加できる
    dict_list = {"x": 10, "z": 30}
    dict_list[1] = 100
    dict_list["hello"] = "hello"
    # d = {"x": 50, "z": 200}
    # 元々あるもの"x""z"に新しく入れると上書きされる
    print(type(dict_list))
    print(dict_list)


set_dict()
