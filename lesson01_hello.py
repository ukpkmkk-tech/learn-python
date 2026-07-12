from itertools import repeat  # 这是注释，python用 # 号注释
print("Hello World") # print()是输出函数
print("\n我开始学习 python 了！")
 # 变量赋值
name = "小明"         # 字符串 str
age = 25             # 整数 int
height = 1.75        # 浮点数 float
is_student = True    # 布尔值 bool

 # 查看类型用 type()
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>

 # 多重赋值(python 特色)
a,b,c = 1,2,3
x = y = 10           # 链式赋值
 # 算数运算符
print(7 + 2)        # 9  加
print(7 - 2)        # 5  减
print(7 * 2)        # 14 乘
print(7 / 2)        # 3.5 除(返回float)
print(7 // 2)       # 3  整除
print(7 % 2)        # 1  取余
print(7 ** 2)       # 49 幂运算

 # 字符串运算
greet = "Hello" + " " + "Python"    # 拼接
repeat = "Hi" * 3                   # HiHiHi 重复
print(repeat)
print(greet)

 # input() 接收用户输入(返回字符串)
name01 = input("请输入你的名字:")
print("你好," + name01 + "!")
 # f-string 格式化
age01 = int(input("请输入你的年龄："))   # int() 转换成整数
print(f"你好！{name01},你今年{age01}岁了,明年{age01 + 1}岁")