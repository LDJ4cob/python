#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

########  Python 打开文件读写的几种形式比较 区别############

   #定义:
    # 1.R(Read)  只读 文件必须要存在 不存在要报错 eg:file("test.txt",'r')
    # 2.r+：可读可写，若文件不存在 报错 并且 以覆盖原文件的形式写入
    # 3.w(Write)  只能写入 不能读 如果文件存在 直接以覆盖原文件的形式写入 如果不存在 则进行新建并写入文件
    # 4.w+ 新建读写 如果文件存在 直接以覆盖原文件的形式写入 如果不存在 则进行新建并写入文件
    # 5.a(Add)：附加写方式打开 不可读  文件不存在 新建 并写入 文件存在 以附加的形式写入
    # 6.a+(Add)：附加读写方式打开 不可读  文件不存在 新建 并写入 文件存在 以附加的形式写入
   #区别:
    #########################################################
    ###     模式	可做操作	若文件不存在	是否覆盖  ###
    ###     r		只能读			报错		-         ###
    ###     r+	    可读可写		报错		是        ###
    ###     w		只能写			创建		是        ###
    ###     w+　	可读可写		创建		是        ###
    ###     a　　	只能写			创建		否，追加写###
    ###     a+	    可读可写		创建		否，追加写###
    #########################################################
print "欢迎光临安全牛技术课题"

choice=raw_input("请输入你要进行的操作:1.登录 2.注册 3.退出")

if choice=='1':
        # 去除用户名 以及 密码 使得用户正常登陆
    print "欢迎光临安全牛技术课堂！ 请输入用户名和密码"
    userName=raw_input("userName:")
    userPassword=raw_input("userPassword:")
    with open("user.txt",'r') as f:
        for i in f.readlines():
            if userName==i.strip('\n').split(";")[0] and userPassword==i.strip('\n').split(";")[1]:
                print "登录成功！"
                exit(2000)
            else:
                print "用户名或密码错误！请重新输入！"
                exit(3000)
elif choice=='2':
    print "欢迎注册安全牛课堂"
    userName=raw_input("请输入用户名:")
    userPassword=raw_input("请输入密码:")
    if userName!=''and userPassword!='':
        print "注册成功"
        userDetails=userName+";"+userPassword
        print userDetails
        # 打开文件的方式 以及 区别 在代码头部
        file=open("user.txt",'a+')
        file.write(userDetails + '\n')
        file.close()
        print "恭喜你注册成功！"
    else:
        print "你输入的信息有误，请重新输入！"



else:
    print "已安全退出，欢迎下次光临"
    exit(1000)
