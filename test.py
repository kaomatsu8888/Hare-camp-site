# Pythonでのproc(n)関数の定義
def proc(n):
    if n == 0:
        return
    else:
        print(n, end="")  # nを印字する
        proc(n - 1)  # proc(n-1)を呼び出す
        print(n, end="")  # 再帰から戻った後にnを印字する


# proc(5)を実行して、印字される数字を観察する
proc(5)
