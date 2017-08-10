__author__ = '陈磊'
import easygui,random
# flavor = easygui.buttonbox('你喜欢哪种口味的冰淇淋？',choices=['草莓味','巧克力味','西瓜味'])
# easygui.msgbox('你的选择是' + flavor)
# flavor_1 = easygui.choicebox('你喜欢哪种口味的冰淇淋？',choices=['草莓味','巧克力味','西瓜味'])
# easygui.msgbox('你的选择是' + flavor_1)
# flavor_2 = easygui.enterbox('你喜欢哪种口味的冰淇淋？')
# easygui.msgbox('你的选择是' + flavor_2)
secrt = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox('''你好，我是猜数字机器人，现在我有一个秘密的数字！
这个数字范围是从1到99，我会给你6次机会。''')
while guess != secrt and tries < 6:
    guess = easygui.integerbox('你猜的数字：')
    if not guess: break
    if guess < secrt:
        easygui.msgbox(str(guess) + '低了')
    elif guess > secrt:
        easygui.msgbox(str(guess) + '高了')
    tries = tries + 1
if guess == secrt:
    easygui.msgbox('恭喜你，答对了！')
else:
    easygui.msgbox('没有机会了，正确的答案是：' + str(secrt))