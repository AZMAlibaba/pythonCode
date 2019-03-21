#!/usr/bin/python3
# encoding=utf-8
# 屏幕中央打印内容
sentence = input("Please input your sentence:")
# 显示屏幕大小 一般设置在80，当然有可能比这个大
screen_width = 80
# sentence的大小(就是长度)
text_width = len(sentence)
# 计划句子与边缘相隔3个单位的长度
box_width = text_width + 6
margin_width = (screen_width - box_width) // 2
# 在屏幕上显示的效果
print(' '*margin_width+'+'+'-'*(box_width - 2)+'+')
print(' '*margin_width+'|'+'-'*(box_width - 2)+'|')
print(' '*margin_width+'|'+' '*2+sentence+' '*2+'|')
print(' '*margin_width+'|'+'-'*(box_width - 2)+'|')
print(' '*margin_width+'+'+'-'*(box_width - 2)+'+')