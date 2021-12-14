# class oldshouji():
#     pinpai=""
#     def setpinpai(self,pp):
#         self.pinpai=pp
#     def getpinpai(self):
#         return self.pinpai
#     def show(self,name):
#         print("正在使用",self.pinpai,"牌的手机给",name,"打电话")
# o=oldshouji()
# o.setpinpai("苹果")
# o.show("刘晓霞")
# class new(oldshouji):
#     def show(self,name):
#         print("语音拨号中..")
#         super().show(name)
#         print("品牌为",self.pinpai,"的手机很好用")
# o=new()
# o.setpinpai("小米")
# o.show("刘晓雪")
#
#
#
# class chushi():
#     name=""
#     age=0
#     def setname(self,n):
#         self.name=n
#     def getname(self):
#         return self.name
#     def  setage(self,a):
#         self.age=a
#     def getage(self):
#         return  self.age
#     def fan(self):
#         print(self.name,"蒸饭")
# class cai(chushi):
#     def chao(self):
#         print(self.name,"烧菜")
# class sun(cai):
#     def a(self):
#         print(self.name,self.age)
# s=sun()
# c=cai()
# c.setname("刘备")
# c.setage(35)
# c.chao()
#
#
#
# class people():
#     name=""
#     age=0
#     sex=""
#     def setname(self,n):
#         if n =="":
#             print("必须填，不能为空")
#         else:self.name=n
#     def getname(self):
#         return self.name
#     def setage(self,a):
#         if a ==0:
#             print("不能为0")
#         else:self.age=a
#     def getage(self):
#         return self.age
#     def setsex(self,s):
#         if s =="男"or s=="女":
#             self.sex=s
#         else:print("别瞎填")
#     def getsex(self):
#         return self.sex
# class huo(people):
#     def ganhuo(self):
#         print("姓名：",self.name,"年龄：",self.age,"性别:",self.sex,"在搬砖")
# a=huo()
# a.setname("撒非法")
# a.setsex("男")
# a.setage(25)
# a.ganhuo()
# class student(people):
#     def lenren(self):
#         print("姓名：",self.name,"年龄：",self.age,"性别:",self.sex,"在学习")
#     def sing(self):
#         print("姓名：", self.name, "年龄：", self.age, "性别:", self.sex, "在唱歌")
# a=student()
# a.setname("第三帝国")
# a.setsex("女")
# a.setage(18)
# a.lenren()
# a.sing()





