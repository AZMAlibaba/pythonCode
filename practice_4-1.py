# 对字典的练习  主要构建数据库使用字典的基本方法（字典中的字典）
# phone和address作为字典键，name作为主字典的键

people={
    'anzunming':{
        'phone':'17716632963',
        'address':'nanjin '
    },
    'xijinping':{
       'phone':'252522',
        'address':'2338411'
    }
}
name=input("Name:")

labels={
    'phone':'phone number',
    'address':'address'
}

request=input('Phone number(p) or address(a):')

if request=='p':
    key='phone'
if request=='a':
    key='address'

if name in people:
    print("{}'s {} is {}".format(name,labels[key],people[name][key]))