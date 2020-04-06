def set_dict():
    dict_list = {"x": 10, "z": 30}  # dict型を色々追加できる
    dict_list[1] = 100
    dict_list["hello"] = "hello"
    print(type(dict_list))
    print(dict_list)
    # 元々あるもの"x""z"に新しく入れると上書きされる d = {"x": 50, "z": 200}


set_dict()
