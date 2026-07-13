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

 # 三、While 循环

count = 0
while count < 3:
     print(f"第{count+1}次")
     count += 1

 # 四、break和continue
 # break:立即跳出整个循环
for i_2 in range(10):
    if i_2 ==6:
        break
    print(i_2)
 # continue:跳过本次,继续下次
for i_3 in range(10):
    if i_3 == 4:
        continue
    print(i_3)
 # 字符串进阶
 # 1、索引 (取一个字符)
s = "Hello,Python"
print(s[0])
print(s[1])
print(s[-2])
print(s[-3])

 # 2、切片 (取一段字符)
 # 格式:s[起,止],包含起,不包含止
print(s[0:2])           # Hello    前 2 个字符
print(s[7:])            # Python   从第 7 个到末尾
print(s[:5])            # Hello    从头到第 5 个
print(s[-6:])           # Python   最后 6 个字符
print(s[:])             # Hello, Python  完整复制

 # 3、常用字符串
s_1 = " Hello,Python "
print(s_1.strip())      # "Hello, Python"  去两端空格
print(s_1.upper())      # 全大写
print(s_1.lower())      # 全小写
print(s_1.replace("Python", "Java"))    # 替换
print(s_1.split(","))   # 按,分割成列表
print(len(s_1))         # 字符串长度
print("Hello" in s_1)   # True 判断是否包含