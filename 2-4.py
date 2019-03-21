#!/usr/bin
# encoding=utf-8

# 提取用户名和PIN码
dataBase = [['albet','1234'],['anzunming','1234'],['cjc','25894']]
usr_name = input('Usr name:')
usr_pin = input('Usr PIN:')
if([usr_name,usr_pin] in dataBase):
        print('Access grantd')
else:
    print('error')