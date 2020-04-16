# pythonではリストをデフォルト引数に与えてはいけない！！バグに繋がるから
# この場合の出力結果は[100, 200]となる同じリスト内に出力されてしまう。
# １、なぜか？pythonはtest_funcのデフォルト引数のl=[]を１どだけ生成する「参照渡し」


def test_func(x, l=[]):
    l.append(x)
    return l


# 2、ここを処理した際はl=[]はまだ空なので実行できる
r = test_func(100)
print(r)

# 3,ここを実行するとdef test_func(x, l=[]):のl=[]の先頭を指したままなので
# ２、の実行した時の参照渡しのlを指しているので、さらに100を追加していることになる。
r = test_func(200)
print(r)


# 解決するには
def test_func1(x, l=None):
    # 何も渡されない場合はNoneとなりプログラムの中だけでからのリストを初期化して渡してくれる。
    if l is None:
        l = []
# 何か渡された場合はappend()で追加
    l.append(x)
    return l


r = test_func1(100)
print(r)
r = test_func1(100)
print(r)
