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

 # ============================================================
 # while 循环
 # ============================================================
 # while 适合"不知道循环多少次"的场景,只要条件为True就一直执行
 # 一定要记得在循环体里改变条件变量,否则会变成死循环!

 # 示例1:计算 1+2+3+...+100 的和
n = 1
total = 0
while n <= 100:
    total += n      # 等价于 total = total + n
    n += 1          # 别忘了让 n 自增,否则 n 永远 <= 100,死循环!
print(f"1到100的和是:{total}")   # 5050

 # 示例2:while True 死循环 + break 退出
 # 常用于"重复执行,直到满足条件才停止"的场景
while True:
    answer = input("请输入 'quit' 退出循环:")
    if answer == "quit":
        print("已退出")
        break       # break:立即跳出整个循环
    print(f"你输入的是:{answer}")

 # ============================================================
 # break 和 continue 的区别
 # ============================================================
 # break    : 跳出【整个】循环,不再执行后续循环
 # continue : 跳过【本次】循环剩余代码,直接进入下一次循环

 # break 示例:找到第一个能被7整除的数就停止
for num in range(10, 50):
    if num % 7 == 0:
        print(f"找到第一个能被7整除的数:{num}")   # 14
        break

 # continue 示例:打印1-10中的奇数(跳过偶数)
for i in range(1, 11):
    if i % 2 == 0:
        continue    # 偶数就跳过,不执行下面的print
    print(i)        # 只会打印 1 3 5 7 9

 # ============================================================
 # 循环嵌套
 # ============================================================
 # 外层循环每执行一次,内层循环要完整执行一遍
 # 注意:嵌套层数不宜过多,一般不超过3层

 # 示例1:打印直角三角形
print("--- 直角三角形 ---")
for i in range(1, 6):       # 外层控制行数
    for j in range(i):      # 内层控制每行*的个数
        print("*", end="")  # end="" 表示不换行
    print()                 # 一行打印完,换行

 # 示例2:经典——九九乘法表
print("--- 九九乘法表 ---")
for i in range(1, 10):          # i 是行,也是乘法表第二个数
    for j in range(1, i + 1):   # j 是列,从1到i
        print(f"{j}×{i}={i*j}", end="\t")  # \t 是制表符,对齐用
    print()                     # 每行结束换行

 # 示例3:用while实现九九乘法表(体会两种循环的区别)
print("--- while版九九乘法表 ---")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}×{i}={i*j}", end="\t")
        j += 1
    print()
    i += 1

 # ============================================================
 # for...else / while...else (了解即可,实际用得少)
 # ============================================================
 # else 块只有在循环【没有被 break 打断】时才会执行
 # 适用场景:查找某个元素,循环结束没找到时做提示

for num in range(2, 10):
    if num == 5:
        print("找到了5")
        break
else:
    print("没找到5")   # 因为break了,所以这行不会执行

 # 对比:没被break打断,else会执行
for num in range(2, 10):
    if num == 99:      # 永远不会满足
        break
else:
    print("循环正常结束,没遇到break")   # 会执行

 # ============================================================
 # 综合练习:猜数字游戏
 # ============================================================
import random   # 导入随机数模块
answer = random.randint(1, 100)   # 生成1-100的随机整数
count = 0

print("====== 猜数字游戏 ======")
while True:
    guess = int(input("请猜一个1-100的数字:"))
    count += 1

    if guess < answer:
        print("小了,再大一点")
    elif guess > answer:
        print("大了,再小一点")
    else:
        print(f"恭喜!你用了{count}次猜中了答案{answer}")
        break