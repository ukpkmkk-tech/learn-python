 # 简易计算器
print("======简易计算器======")
num1 = float(input("请输入第一个数字："))
operate = input("请输入运算符")
num2 = float(input("请输入第二个数字："))

if operate == "+":
    result = num1 + num2
elif operate == "-":
    result = num1 - num2
elif operate == "*":
    result = num1 * num2
elif operate == "/":
    if num2 == 0:
        result = "错误：除数不能为0"
    else:
        result = num1 / num2
else:
    result = "不支持的运算符"

print(f"计算结果：{num1} {operate} {num2} = {result}")