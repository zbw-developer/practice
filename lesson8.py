def say_hello():
    print("你好")

say_hello()

def greet(name):
    print(f"你好,{name}")

greet("zbw")
greet("小明")

def add_print(a,b):
    print(a+b)

def add_return(a,b):
    return a + b

def find_max(numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

print(find_max([3,6,9,2,1]))
print(find_max([-6,-12,-56]))
print(find_max([233]))
print(add_return(3, 5) + 100)