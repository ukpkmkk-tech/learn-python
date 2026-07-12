 # 条件判断 if / elif / else
age = 25
if age >= 18:
    print("你已成年")

age01 = 16
if age01 >= 18:
    print("成年")
else:
    print("未成年")

score = 11
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

 # 比较运算符
 # ==	等于	5 == 5	True
 # !=	不等于	5 != 3	True
 # >	大于	5 > 3	True
 # <	小于	5 < 3	False
 # >=	大于等于	5 >= 5	True
 # <=	小于等于	5 <= 3	False

 # 逻辑运算符 and / or / not
age02 = 10
has_id = False

 # and:两个都满足才True
if age02 >= 18 and has_id:
    print("可以进入")

 # or:满足一个就True
if age02 < 12 or age02 > 60:
    print("半价票")
else:
    print("成人票")

 # not:取反
if not has_id:
    print("请出示证件")
else:
    print("请进")

 # 成员运算符 in
fruits = ["苹果", "香蕉", "橘子"]
if "西瓜" in fruits:
    print("有苹果")
else:
    print("没有这个水果")


 # 循环：for
 # 1、 for 遍历序列
 # 遍历字符串的每一个字符
for char in "python":
    print(char)
 # 输出:P y t h o n(每个字符一行)

 #　遍历列表
for fruit in fruits:
    print(fruit)

 # 2、 range() 生成数字序列
 # range() 是最常用的循环工具,有三种用法:
 # 一个参数:从 0 到 n-1
for i in range(5):
    print(i)
 # 两个参数：从 start 到 stop-1
for i_0 in range(1,6):
    print(i_0)
 # 三个参数: 从 start 到 stop-1,步长 step
for i_1 in range(0,10,2):
    print(i_1)
 # 倒序:步长为负
for i_2 in range(10,0,-1):
    print(i_2)