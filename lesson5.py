import random

target = random.randint(1,100)
count = 0

while True:
    guess = int(input("猜一个 1-100 的数:"))
    count = count + 1

    if guess > target:
        print("大了")
    elif guess < target:
        print("小了")
    else:
        print(f"对了!你猜对了{count}次")
        break