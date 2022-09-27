from random import randint
import datetime

ans_list=[
    ["サザエさんの旦那は？",('ますお','マスオ')],\
    ["カツオの妹の名前は？",('わかめ','ワカメ')],\
    ["タラオはカツオから見てどんな関係？",('おい','甥','甥っ子','おいっこ')]
    ]
num = randint(0,2)

def shutudai():
    print("問題：\n"+ans_list[num][0])

def kaito():
    st = datetime.datetime.now()

    ans = input("答えるんだ：")
    if ans in ans_list[num][1]:
        print("正解")
    else:
        print("出直してこい")
    ed = datetime.datetime.now()
    print((ed-st).seconds)

if __name__ == "__main__":
    shutudai()
    kaito()