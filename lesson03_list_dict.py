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

 # 列表:增删改查
fruits_2 = ["苹果","香蕉","橘子"]

 # 1、增加元素
 # append():在末尾增加一个
fruits_2.append("西瓜")
print(fruits_2)

 # insert():在指定位置插入
fruits_2.insert(1,"葡萄")
print(fruits_2)

 # extend():合并另一个列表
more = ["荔枝","草莓"]
fruits_2.extend(more)
print(fruits_2)

 # 2、删除元素
 # remove():按值删除(只删除第一个匹配的)
fruits_2.remove("葡萄")
print(fruits_2)

 # pop():按索引删除,并返回被删除的值
removed = fruits_2.pop(2)
print(removed)

 # pop() 不传参:删除最后一个
last = fruits_2.pop()
print(f"删除的最后一个是{last}")

 # del:用关键字删除
del fruits_2[1]
print(fruits_2)

# clear():清空整个列表
# fruits_2.clear()  # 慎用,会清空!

 # 3、修改元素
nums = [10,20,30,40,50]
nums[0] = 100       # 修改单个
nums[1:4] = [200,300]
print(nums)

 # 4、查询元素
print("香蕉" in fruits_2)         # True/False 判断是否存在
print(fruits_2.count("苹果"))     # 统计某元素出现次数
print(fruits_2.index("苹果"))     # 查找元素索引(找不到会报错)

 # 5、排序
nums_2 = [3,1,4,1,2,5,6,0]
nums_2.sort()                    # 升序(源列表改变)
print(nums_2)
nums_2.sort(reverse=True)        # 降序
print(nums_2)

 # sorted():返回新列表,不改变源列表
nums_3 = [4,3,1,2]
new_list = sorted(nums_3)
print(new_list)                  # [1, 2, 3, 4]
print(nums_3)                    # [4, 3, 1, 2]

 # reverse():反转列表
nums_3.reverse()
print(nums_3)

 # 6、遍历列表
 # 方式一:直接遍历列表
for f in fruits_2:
    print(f)

 # 方式二:同时取索引和值(enumerate)
for index,value in enumerate(fruits_2):
    print(f"第{index + 1}个水果是{value}")

 # 7、列表推导式
 # 传统写法
squares = []
for i in range(11):
    squares.append(i**2)
print(squares)

 # 推导式写法(一行搞定)
squares_2 = [i ** 2 for i in range(11)]
print(squares_2)

 # 带条件的推导式
even = [i ** 2 for i in range(11) if i % 2 == 0]
print(even)