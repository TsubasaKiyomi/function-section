# 辞書型のコピー
def argument_number_list(**arg):
    v = "a", "b", "c"
    return v


# .copyがされれば、新しく入れた{"hello": "python"}はcopy_listのみの出力結果となる
# .copyをしなかった場合argument = copy_listにした場合はどちらも同じ出力結果となる「参照渡し」
argument = {"arg1": "one", "arg2": "two", "arg3": "three"}
argument_number_list(**argument)
copy_list = argument.copy()
argument = copy_list
copy_list = {"hello": "python"}


print(copy_list)
print(argument)
