# 関数定義


def say_something():
    print("hi")


say_something()
print(type(say_something))
# typeは<class 'function'>なので f = にしても出力される。
f = say_something
f()


#####返り値#####

# 関数を呼び出した後に何かを返したい。
def say_something1():
    # "hi"が変数sに入り
    s = "hi"
    # sを返すためにreturnを使う
    return s


# 変数sがresultに入るのでprint()で出力する。
result = say_something1()
print(result)


####　引数　####


# what_is_thisの("red")が引数(color)に入る。
def what_is_this(color):

    # print()の中には"red"が入る
    print(color)


what_is_this("red")


def what_is_this1(color):
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green pepper"
    elif color == "yellow":
        return "lemon"
    else:
        return "i don't know"


# 関数定義をしてファンクションを呼び出せる。
result1 = what_is_this1("green")
result2 = what_is_this1("red")
result = what_is_this1("yellow")
print(result1)
print(result2)
print(result)


# (a: int, b: int)とint型を宣言してもtypeは"str"、エラーも出ないので気をつける。
def add_num(a: int, b: int) -> int:
    return a + b


r = add_num("a", "b")
print(type("a"))
