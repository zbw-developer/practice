import random

def play_game():
    target = random.randint(1,100)
    count = 0

    while True:
        guess = int(input("猜一个数[1-100]:"))
        count = count + 1

        if guess < target:
            print("小了")
        elif guess > target:
            print("大了")
        else:
            print(f"猜对了,猜了{count}次")
            break
        
play_game()
play_game()
play_game()