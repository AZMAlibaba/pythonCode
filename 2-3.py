#!/usr/bin python3
# encoding=utf-8

# 在屏幕的正中央打印句子
sentence = input("Sentence:")
# 但是有的句子长度会大于80  这时程序可能出现崩溃
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
margin_width = (screen_width - box_width) // 2
print(' '*margin_width+'+'+'-'*(box_width-2)+'+')
print(' '*margin_width+'|'+' '*(box_width-2)+'|')
print(' '*margin_width+'|'+' '*2+sentence+' '*2+'|')
print(' '*margin_width+'|'+' '*(box_width-2)+'|')
print(' '*margin_width+'+'+'-'*(box_width-2)+'+')