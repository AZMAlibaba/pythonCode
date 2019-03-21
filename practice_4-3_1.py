# 用字典建立一个小的基本数据库
people={
    'anzunming':{
        'phone':'177166632963',
        'address':'贵州省思南县杨家坳乡'
    },
    'zhangaiqian':{
        'phone':'177xxxxxxxx',
        'address':'贵州省德江县'
    }
}

name=input("Please input you want index name:")

request=input("Index phone(p) or address(a)?:")

labels={
    'p':'phone',
    'a':'address'
}

if name in people:
    print("{}'s {} is {}".format(name,labels[request],people[name][labels[request]]))