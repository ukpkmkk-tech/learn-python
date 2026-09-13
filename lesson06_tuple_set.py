# 第 6 课:元组 Tuple + 集合 Set
# 元组:有序、不可变 → "上了锁的列表",用 ( )
# 集合:无序、不重复 → "自动去重的袋子",用 { }

# ═══════════ 上半场:元组 Tuple ═══════════

# 一、创建元组
t = (1,2,3)
point = (100,200)       # 坐标就适合用元组:x 和 y 是一组固定的数
single = ("苹果",)
print(type(t))          # <class 'tuple'>
print(point)            # (100, 200)

#  单元素组的坑:必须多写一个逗号！
not_tuple = (5)         # 括号被当成数学括号,这是数字5
is_tuple = (5,)         # 逗号告诉python:这是元组
print(type(not_tuple))  # <class 'int'>
print(type(is_tuple))   # <class 'tuple'>

# 二、元组的访问:和列表一模一样(索引、切片全能用)
fruits = ("apple", "banana", "cherry")
print(fruits[0])        # apple
print(fruits[-1])       # cherry
print(fruits[0:2])      # ('apple', 'banana') 切片出来的还是元组

# 三、元组的核心特性:不可变！(和列表最大的区别)
# fruits[0] = "watermelon" # <-取消注释会报错
# TypeError: 'tuple' object does not support item assignment
# 翻译:元组不许改！这是"锁"

# 但注意:锁的是"元组里装的东西不变",不是"不能重新赋值整个变量"
fruits = ("apple", "banana", "orange")  # 这行合法,是换了个元组,不是改旧的

# 四、为什么要用元组？(列表不是挺好的吗)
# 1、数据不该改时用元组:坐标、星期几、配置项 －－防止手滑改掉
# 2、占内存小、速度快
# 3、字典的键必须是不可变的 ->列表不能当键,元组可以！
locations = {(39.9,116.4):"北京",(31.2,121.5):"上海"}
print(locations[(31.2,121.5)])      # 上海

# 五、解包:元组"拆开"赋值
x,y = (100,200)     # 一口气拆给两个变量
print(x)            # 100
print(y)            # 200

# 想起什么了吗?lesson05 的这句:
#   for key, value in student.items():
# key 和 value 每轮拿到的就是一个个 (键, 值) 元组,被解包了!

# 函数返回多个值是,返回的也是元组
def min_max(nums):
    return min(nums), max(nums)     # 看似返回两,实际返回一个元组

result = min_max([3,1,4,1,5])
print(result)       # (1, 5)
low, high = min_max([3,1,4,1,5])
print(f"最低{low},最高{high}")      # 最低1,最高5

# ═══════════ 下半场:集合 Set ═══════════

# 六、创建集合
s = {1,2,3}
print(type(s))      # <class 'set'>

# ⚠️ 坑:空的大括号是字典!空集合要用 set()
not_set = {}                # 这是字典!
real_set = set()            # 这才是集合
print(type(real_set))       # <class 'set'>
print(type(not_set))        # <class 'dict'>

# 七、集合的杀手锏:自动去重
nums = [1,3,2,3,1,5,3]      # 一堆重复的
unique = set(nums)     # 一秒去重
print(unique)               # {1, 2, 3, 5}
# print(type(unique))         <class 'set'>
# 注意:无序!打印的顺序可能和插入的顺序不同,这是正常的

# 去完重还想要有序?套一个sorted()(lesson03 的老朋友)
print(sorted(unique))       # [1, 2, 3, 5]
# print(type(sorted(unique))) <class 'set'>

# 八、集合基本操作
colors = {"red", "green", "blue"}
colors.add("yellow")        # 增(注意是 add,不是 append!)
colors.remove("red")        # 删(删不存在的会报错)
colors.discard("purple")    # 删(删不存在的也不报错,更安全)
print(colors)               # {'green', 'yellow', 'blue'}

print("blue" in colors)     # True 集合查"在不在"特别快

# 九、集合的数学魔法:交集 / 并集 / 差集
my_friends = {"dc","lzy","xy","hh"}
your_friends = {"lzy","xy","mm"}
print(my_friends & your_friends)        # {'xy', 'lzy'}
print(my_friends | your_friends)        # {'hh', 'dc', 'mm', 'xy', 'lzy'}
print(my_friends - your_friends)        # {'hh', 'dc'}

# 十、三大容器总复习(背下来)
# 列表 [ ]  有序、可变、可重复 -> 按编号取       一串东西
# 元组 ( )  有序、不可变、可重复 -> 按编号取      不许改的一串
# 字典 { }  键值对、可变      -> 按键值        名字 -> 值
# 集合 { }  无序、不可重复    ->  不能按位置取   只要"有没有"

# =======课后作业=======

# 作业1
names = ["dc", "lzy", "dc", "xy", "lzy", "hh"]
unique_names = set(names)
print(unique_names)
print(sorted(unique_names))

# 作业2
a_group = {"dc", "lzy", "xy"}
b_group = {"lzy", "mm", "xy"}
print(a_group & b_group)
print(a_group - b_group)
print(a_group | b_group)
print(len(a_group | b_group))

# 作业3
nums_4 = [4, 8,4, 1, 8, 9]
def analyze(nums):
    return len(set(nums)),min(nums), max(nums)

f,g,h = analyze(nums_4)
print(f"去重后共{f}个,最大{h},最小{g}")