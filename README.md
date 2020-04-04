##### Function とは

- 関数のこと

##### 関数とは

- ある特定の処理をひとまとまりした物

##### 関数宣言

- 基本の形

```
def 関数宣言(引数１・２、、、、):
    print('hello')

関数宣言()

```

- 引数のない場合

```
・numと言う"関数"を宣言

def num():
    print('hello')
num()

# hello
```

- 引数がある場合

```
def num(a,b):
    print(a*b)
num(2,5)

・引数(a,b)に(2*5)を代入し呼び出している
#10
```

- 戻り値のない場合

```
def hello():
    print('hello')
hello()
# hello
```

- 戻り値のある場合

```
def num(a,b):
    c = a*b
    return c
print(num(2,5))
# 10
```

#### return の使い方

- return は出力するためではなく他の関数でその戻り値を使う場合に用いる

```
def hello():
    return 'hello'

def num():
    a = hello()
    return a + ' '+'world'

print(num())
# hello world
・def num()でdef num()の戻り値であるhelloを再利用できた。
```

#### \*args と\*\*kwargs

- 関数定義で引数に\*と\*\*（1 個または 2 個のアスタリスク）をつけると、任意の数の引数（可変長引数）を指定することができる
- \*と\*\*が頭についていれば他の名前でも問題ない。

- to_split「分割」
