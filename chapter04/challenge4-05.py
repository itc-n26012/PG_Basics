def decimal(a):
    try:
        print("入力された文字=",a)
        print("入力された文字を小数点化した結果=",float(a))
        return a
    except ValueError:
        print("誠意数、または、小数点を入力してください。")

#a = srt(4)
#a = str("あ")
a = str("")
decimal(a)
