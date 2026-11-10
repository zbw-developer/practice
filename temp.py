def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

value = float(input("请输入温度："))
unit = input("输入单位(C 或 F):")

if unit == "C":
    result = c_to_f(value)
    print(f"{value}°C = {result}°F")
else:
    result = f_to_c(value)
    print(f"{value}°F = {result}°C")