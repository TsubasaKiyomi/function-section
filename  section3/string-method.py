def smethod(a, b, c):
    d = a+b+c
    return d


each_method = smethod("etest", " ftest", " gtest")
print(each_method.capitalize())  # 最初の文字のみ大文字
print(each_method.upper())  # 全て大文字
print(each_method.lower())  # 全て小文字
print(each_method.title())  # 先頭文字が大文字
print(each_method.replace("etest", "テスト"))
