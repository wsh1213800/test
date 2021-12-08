import random

bank = {'1': {'username': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
              'bank_name': '中国工商银行', 'money': 1000},
        '2': {'username': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
              'bank_name': '中国工商银行', 'money': 0}}
bank_name = "中国工商银行"


def useradd():
    account = str(random.randint(10000000, 99999999))
    username = input("请输入您的姓名")
    password = input("请输入您的密码")  # 如果定义为str   ”“
    country = input("\t\t请输入您的国家")  # \t表示一个tab
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入你的街道")
    door = input("\t\t请输入您的门牌号")
    gift = bankadd(account, username, password, country, province, street, door)  # 位置对应
    if gift == "1":
        print("开户成功,一下是您的详细信息")
        # 模板
        info = '''
                --------工商银行-------
                    1、账号：%s
                    2、姓名：%s
                    3、密码：******
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
        '''
        print(info % (account, username, country, province, street, door, bank[account]["money"]))
        print(bank)
    elif gift == "2":
        print("请使用其他用户")
    elif gift == "3":
        print("数据库已满")


# 往字典里面存数据
def bankadd(account, username, password, country, province, street, door):
    if account in bank:  # 姓名在不在bank的键里
        return "2"
    elif len(bank) >= 100:
        return "3"
    bank[account] = {
        "username": username,  # 从useradd的account获取的随机数
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name,
        "money": 0
    }
    return "1"


def storage(ca, cb):  # 存钱
    if ca in bank:
        bank[ca]['money'] += cb
        print("存钱成功，账户余额为" + str(bank[ca]['money']))
    elif ca not in bank:
        return False
    print(bank)


def withdraw(qa, qb, qc):  # 取钱
    if qa not in bank:
        return "1"
    elif qa in bank:
        if qb == bank[qa]['password']:
            if bank[qa]['money'] >= qc:
                bank[qa]['money'] -= qc
                print("取钱成功，账户余额为" + str(bank[qa]['money']))
                return "0"
            else:
                return "3"
        else:
            return "2"
    print(bank)


def transfer_accounts(za, zb, zc, zd):  # 转账
    if za != zb:
        if za in bank:
            if zb in bank:
                if zc == bank[za]['password']:
                    if bank[za]['money'] >= zd:
                        bank[za]['money'] -= zd
                        bank[zb]['money'] += zd
                        print("转账成功，账户余额为" + str(bank[za]['money']))
                        print("收到转账，账户余额为" + str(bank[zb]['money']))
                    else:
                        return "3"
                else:
                    return "2"
            else:
                return "1"
        else:
            return "1"
    elif za == zb:
        print("转出账号不能和转入账号相同")


def inquire(cxa, cxb):  # c查询
    if cxa in bank:
        if bank[cxa]['password']==cxb:
            print("查询成功,以下是您的详细信息")
            information = '''
                            --------工商银行-------
                                1、账号：%s
                                2、姓名：%s
                                3、密码：******
                                4、国家：%s
                                5、省份：%s
                                6、街道：%s
                                7、门牌：%s
                                8、余额：%s
                            '''
            print(information % (
            cxa, bank[cxa]["username"], bank[cxa]["password"], bank[cxa]["province"],
            bank[cxa]["street"], bank[cxa]["door"], bank[cxa]["money"]))
        else:
            print("密码不正确")
    else:
        print("该账户不存在")


print("********************")
print("*  中国工商银行    *")
print("*  账户管理系统    *")
print("*     V1.0         *")
print("********************")
print("*1,开户")
print("*2,存钱")
print("*3,取钱")
print("*4,转账")
print("*5,查询")
print("*6,Bye")
print("********************")


def access():
    while 1:

        business = input("请选择您要办理的业务")
        if business == "1":
            useradd()
        elif business == "2":
            ca = input("请输入你的账号")
            cb = int(input("请输入你存取的金额"))
            cs = storage(ca, cb)
            if cs == False:
                print("没有该账户")
        elif business == "3":
            qa = input("请输入你的账号")
            qb = input("请输入你的密码")
            qc = int(input("请输入你的取钱金额"))
            qw = withdraw(qa, qb, qc)
            if qw == "1":
                print("账户不存在")
            elif qw == "2":
                print("密码错误")
            elif qw == "3":
                print("余额不足")
        elif business == "4":
            print("转账汇款须谨慎，谨防电信诈骗")
            za = input("请输入转出的账号")
            zb = input("请输入转入的账号")
            zc = input("请输入账号密码")
            zd = int(input("请输入转出金额"))
            zt = transfer_accounts(za, zb, zc, zd)
            if zt=="1":
                print("账号不存在")
            elif zt=="2":
                print("密码错误")
            elif zt == "3":
                print("余额不足")
        elif business == "5":
            cxa = input('请输入用户账号')
            cxb= input('请输入用户密码')
            inquire(cxa, cxb)
        elif business == "6":
            print("欢迎您下次再来，亲")
            exit()
        else:
            print('请输入正确的序号')


access()
