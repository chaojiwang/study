
import random
secret = random.randint(1,99)
guess = 0
tries = 0
print('你好，我是猜测游戏机器人，我有个秘密的数字。')
print('数字是1到99，我会给你6次机会。')
while guess != secret and tries < 6:
    guess = int(input('你猜的数字：'))
    if guess < secret:
        print('低了')
    elif guess > secret:
        print('高了')
    tries = tries + 1
if guess == secret:
    print('恭喜你，猜对了！！！')
else:
    print('很遗憾，没能猜对！')
    print('这个数字是：',secret)