# 辞書型のコピー
def multiple_argument(**a):
    v = "a", "b", "c"
    return v


# .copyがされれば、新しく入れた{"hello": "python"}はcopy_listのみの出力結果となる
nombers_list = {"No1": "one", "No2": "two", "No3": "three"}
multiple_argument(**nombers_list)


# .copyをしなかった場合argument = copy_listにした場合はどちらも同じ出力結果となる「参照渡し」
copy_list = nombers_list.copy()
argument = copy_list
copy_list = {"hello": "python", "copy": "list"}


print(argument)
print(copy_list)
print(copy_list.keys())
print(copy_list.values())
