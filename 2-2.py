#!/usr/bin python3
# coding=utf-8
#提取域名：类似于http://www.somedomain,com的URL中提取域名
url = input('Please enter the URL:')
domain = url[11:-4]
print("Domain name:"+domain)