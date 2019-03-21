#!/usr/bin
# encoding=utf-8
# 一个简单的数据库
# 将一个人名用作键的字典，每一个人都用一个字典表示
# 字典包含phone和address他们分别与电话号码和地址相联
people={
    'Alic':{
        'phone':'17716632963',
        'address':'fjkdhk vkjdsvk'
    },
    'Bobu':{
        'phone':'255825',
        'address':'vnm sjvcs'
    }
}

# 电话和地址描述性标签，供打印输出是使用
labels={
    'phone':'phoneNumber',
    'address':'address'
}
name=input('Name:')
request=input('Phone number(p) or address(a):')

# 使用正确的键
if request=='p':
    key='phone'
if request=='a':
    key='address'
# 仅当名字是字典包含的键时才打印信息
if name in people:
    print("{}'s {} is {}".format(name,labels[key],people[name][key]))