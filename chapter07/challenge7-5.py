#無限ループする数当てプログラム
answers = [23, 6, 19, 37, 43]  #正解の数

#無限ループさせる
while True:
    #何か数字を入力してもらう
    n = input("")
    #"q"が入力されていたら終了
    if n == "q":
        #無限ループから強制的に抜ける
        break

    else:
        if int(n) in answers:
            print("正解")
        else:
            print("数字を入力するか、qで終了します")
