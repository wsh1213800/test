'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
'''

import random
#   随机生成数字  （开始int，结束int）  []
rmb=5000
print("要开始游戏吗？开始输入y，不玩输入n")
a=input("y/n")
if a=="y":
    i = 0
    while i<15:
        Ran = random.randint(1, 100)
        print(Ran)
        while 1:
            print(rmb)
            if i == 15:
                print("猜错15次，游戏结束," + str(rmb))
                break
            num=input("请输入一个数字")
            num=int(num)
            if num == Ran:
                print("猜对了")
                rmb+=300
                i=0
                break
            elif num<Ran:
                print("猜小了")
                rmb-=100
                i+=1
            elif num>Ran:
                print("猜大了")
                rmb -= 100
                i += 1
            else:
                print("猜错了")
else:
    print("不玩，滚")