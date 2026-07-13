import random

target = random.randint(1, 100)
count = 0
print("我想了一个 1-100 之间的数字,你来猜猜看!")
while True:
    try:
        guess = int(input("请输入你猜的数字："))
    except ValueError:
        print(f"请输入有效数字！")
        continue
    count += 1
    if guess < target:
        print("小了")
    elif guess > target:
        print("大了")
    else:
        print(f"恭喜你猜对啦!你一共猜了{count}次。")
        break
    if count >= 10:
        print(f"游戏失败！你是猪吗猜了{count}次都猜不对,正确答案是{target}")
        break