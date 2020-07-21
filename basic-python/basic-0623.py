# 関数の説明
# スペースとか、インデントとか、: とか () とか 細かいところまで一緒じゃないと動きません
# tab キーでインデントを入力できます

def test(i):
    if (i % 7 == 0) and (i % 13 == 0):
        print("yeaaaaaaa!!")
    elif i % 7 == 0:
        print("7の倍数!!")
    elif i % 13 == 0:
        print("13の倍数!!")
    else:
        print(i)

def if_test(num):
    for i in range(1, num):
        test(i)

# test(15)
if_test(100)
