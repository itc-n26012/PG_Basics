my_features = {
    "身長": "166cm",
    "好きな色": "緑",
    "好きなアーティスト": "BTS顔",
    "趣味": "音楽鑑賞",
    "出身地": "沖縄県那覇市"
}

print("--- 登録されている辞書データ ---")
print(my_features)
print("-" * 30)

user_key = input("調べたい特徴を入力してください（例: 身長、好きな色）: ")

if user_key in my_features:
    # 辞書にキーが存在する場合、そのバリューを取得して表示
    result_value = my_features[user_key]
    print(user_key + " は「" + result_value + "」です！")
else:
    # 辞書にキーが存在しない場合の案内
    print("そのキーワードは辞書に登録されていません。")
