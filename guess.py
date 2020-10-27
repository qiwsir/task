"""猜数游戏"""
import random

counts = 0
answer = random.randint(1, 100)

while counts >=0:   # //这个条件总成立，没有起到终止循环的判断作用
    temp = input("请输入一个100以内的正整数： ")
    guess = int(temp)

    if guess > 100:    # //还可能小于0，或者含有非数字字符
        print("超出范围啦")
        break     # 不能随便终止，应该允许用户修改错误
        
    else:
        if guess == answer:
            counts = counts + 1
            print("猜中啦！")
            print("你猜了：" + str(counts) + "次")
            break
        else:     # 用多分支，不要嵌套
            if guess < answer:
                print("小了")
                counts = counts + 1
            else:
                print("大了")
                counts = counts + 1

print("游戏结束")
