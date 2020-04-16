# 位置引数
# def menu(entree, drink, dessert):
# print(entree)
# print(drink)
# print(dessert)

# 位置引数を使用しているのでmenu("beef", "beer", "ice")の順番を変えると
# menu(entree, drink, dessert)と中身があべこべになる。
# menu("beef", "beer", "ice")

# キーワード引数


def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


# menu()の順番を変えても、関数定義したmenuの順番通りに出力される。
# キーワード引数と位置引数を合わせて出力できる。


# デフォルト引数
# 関数定義した引数に直接入力することでmenu()に値を返さずに出力できる。
def menu1(entree="beef", drink="beer", dessert="ice"):
    print(entree)
    print(drink)
    print(dessert)


# デフォルト引数を書き換える。


def menu2(entree="beef", drink="beer", dessert="ice"):
    print(entree)
    print(drink)
    print(dessert)


# def menu(entree="beef", drink="beer", dessert="ice"):の引数を書き換える
# beefをchickenに beerをwineに書き換える。


# デフォルト引数・位置引数・キーワード引数をわせて使用できる。
def color(color1="red", color2="紫", color3="black"):
    print(color1)
    print(color2)
    print(color3)


menu(entree="beef", dessert="ice", drink="beer")
menu1()
menu2(entree="chicken", drink="wine")
color("pink", color3="yellow")
