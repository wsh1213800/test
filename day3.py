# 实现输入10个数字，并打印10个数的求和结果
# s = []
# for i in range(10):
#     a=int(input())
#     s.append(a)
# print(sum(s))

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# s = []
# for i in range(10):
#     a=int(input())
#     s.append(a)
# print(max(s),sum(s),sum(s)/10)


# 使用random模块，如何产生 50~150之间的数？
# import random
# a=random.randint(50,150)
# print(a)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，
# 则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）

# a=int(input())
# b=int(input())
# c=int(input())
#
# if a+b>c or a+c>b or b+c>a:
#     if a==b and b==c:
#         print("构成等边三角形")
#     elif a==b or a==c or b==c:
#         print("构成等腰三角形")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or a**2+b**2==c**2:
#         print("构成直角三角形")
#     else:
#         print("构成普通三角形")
# else:
#     print("不能形成三角形")


# 有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56

# A=56
# B=78
# A,B=B,A
# # print(A,B)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# name="root"
# password="admin"
# i=0
# while i<3:
#     a=input()
#     if a!=password:
#         i+=1
#         print("输入错误")

# 编程实现下列图形的打印

# for i in range(8):
#     for j in range(0, 8 - i):
#         print(end=" ")
#     for k in range(8 - i, 8):
#         print("*", end=" ")
#
#     print("")

# 使用while循环实现NxN乘法表的打印。
# i=1
# a=int(input())
# while i<=a:
#     j=1
#     while j<=i:
#         print("%dx%d=%d"%(i,j,i*j),end=" ")
#         j=j+1
#     print(" ")
#     i+=1
#
# 编程实现99乘法表的倒叙打印
# for i in range(9,0 ,-1):
#     for j in range(i,0 ,-1):
#         print("%2d*%2d=%2d"%(i,j,i*j),end="")
#     print("\n")
# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
# a=20
# i=0
# while 1:
#     a-=3
#     if a<0:
#         print(i)
#         break
#     a+=2
#     i+=1

# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# a=int(input())
# n=1
# for i in range(1,a+1):
#     n=n*i
# print(n)