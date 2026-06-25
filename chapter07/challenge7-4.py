
answers = [23, 6, 19, 37, 43]  

while True:

    n = input("数字を入力してください：")
    
    
    if n == "q":
    
        break

    else:
        
        if int(n) in answers:
            print("正解")
        else:
            print("不正解！数字を入力するか、qで終了します")
