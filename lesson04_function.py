# 第 4 课：函数 Function
# 函数 = 打包好的代码块，可以重复调用
# 作用：避免重复代码，让程序更清晰

# 一、定义与调用
# def 函数名():
#     代码块(注意缩进)
def say_hello():
    print("你好！")

# 函数定义后不会执行，必须调用才会运行
say_hello()       # 你好！
say_hello()       # 你好！ 可反复调用


# 二、参数：给函数"喂"数据
def greet(name):
    print(f"Hello {name}!")

greet("李泽宇")     # Hello 李泽宇
greet("董超")      # Hello 董超


# 三、多个参数 + return 返回值
# 对比：greet 只负责打印；add 把结果算好再还给调用处
def add(a,b):
    result  = a + b         # 局部变量，只在函数内有效
    return result           # return 把值"送"回到调用处

sum_1 = add(3,5)      # 拿到add的返回值
print(sum_1)                # 8
print(add(10,20))     # 30也可以直接打印


# 四、没有return的函数，默认返回None
def nothing():
    print("我不返回任何值")

print(nothing())            # 先打印"我不返回任何值"，再打印None

# 五、默认参数：调用时可省略
def welcome(name,city = "北京"):
    print(f"{name} is {city}")

welcome("dc")                       # dc是北京
welcome("lzy" , "sx")    # lzy是sx

# 六、关键字参数：按名字上传，顺序可打乱
def info(name,age,city):
    print(f"{name} is {age} years old,live in {city}")

info(age = 100,name = "dc",city = "sz")

# 七、变量作用域(重点)
# 函数中创建的变量是"局部变量",函数外访问不到
def test():
    x = 10      # 局部变量
    print(x)    # 函数内能访问

test()          # 10
# print(x)      # 取消注释会报错！外面的x不存在

# 定义在函数外的的叫"全局变量",函数内可以读取
num = 100
def show():
    print(num + 1)  # 读取全局变量
show()          # 101

# 函数内修改全局变量,必须加global声明
def change():
    global num
    num = 999

change()
show()
print(num)       # 999 全局变量真的被改了

# 八、把之前学的if装进函数
# 之前你是写在外面的if ,现在包装成函数,随时取用
def get_level(score):
    if score >= 90:
        return "high"
    elif score >= 80:
        return "medium"
    elif score >= 60:
        return "low"
    else:
        return "normal"

print(get_level(95))
print(get_level(82))
print(get_level(75))
print(get_level(45))

# 实验:return当场变成值
def square(x):
    return x * x
print(square(5))
print(square(3) + square(4))
print(square(square(2)) )

# 作业
def countdown(n):
    for i in range(n, 0, -1):
        print(i)
    print("发射！")
countdown(10)
countdown(20)
countdown(3)