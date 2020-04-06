def fruits(a, b, c):
    return a + b + c


each_method = fruits("apple", " banana", " peach")
print(each_method.capitalize())  # 最初の文字のみ大文字
print(each_method.upper())  # 全て大文字
print(each_method.lower())  # 全て小文字
print(each_method.title())  # 先頭文字が大文字
print(each_method.replace("peach", "桃"))
print(each_method.replace("banana", "バナナ"))
