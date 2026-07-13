 # 列表 List  []   有序、可变、可重复    → 类似"抽屉柜"
 # 字典 Dict  {}   键值对、可变         → 类似"标签柜"
 # 创建列表
fruits = ["apple", "banana", "cherry"]
numbers = [1,2,3,4,5,6,7,8,9]
mixed = [1,"hello",True,3.14] # 可以混合类型但不推荐
empty = []                    # 空列表

 # 查看类型和长度
print(type(fruits))           # <class 'list'>
print(len(fruits))            # 3

 # 访问元素(索引从0开始)
fruits_1 = ["苹果", "香蕉", "橘子", "西瓜", "葡萄"]

 # 正向索引
print(fruits_1[0])
print(fruits_1[2])

 # 负向索引
print(fruits_1[-1])
print(fruits_1[-3])

 # 索引越界会报错
 # print(fruits_1[10])
 