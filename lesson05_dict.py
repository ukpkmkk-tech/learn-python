# 第 5 课:字典 Dict
# 字典 = 键值对(key:value)的集合,用{}创建
# 对比:列表像"抽屉柜",按编号0、1、2找
#     字典像"标签柜",按标签(键)直接找
# 格式:{"键":值,"键":值,}

# 一、创建字典
empty = {}              # 空字典

student = {
    "name":"dc",
    "age":200,
    "city":"sz",
}
print(type(student))
print(len(student))

# 注意:键要唯一、且不可变(字符串/数字都行),值可以是任何东西
a = {1:"one",2:"two",3:"three"}

# 二、访问:用键取,像查字典
print(student["name"])
print(student["age"])

# 用不存在的键会报错 KeyError!
# print(student["height"])

# 更安全的访问:.get() --键不存在时返回None,不会报错
print(student.get("height"))
print(student.get("height",0))
print(student.get("name"))

# 三、增/改(同一写法！键不存在 = 新增,键存在 = 覆盖修改)
student["score"] = 100
print(student["score"])

student["age"] = 300
print(student["age"])

# 四、删除
del student["score"]
removed = student.pop("city")
print(removed)
print(student)

# 五、判断键是否存在:用in
print("name" in student)
print("height" in student)
print("score" in student)

# 六、遍历字典(重点！)
# 1、只遍历:直接for字典
for key in student:
    print(key)

# 2、keys() 拿所有键,values() 拿所有值
print(student.keys())
print(student.values())

# 3、items()同时拿键和值(最常用,记住它！)
for key, value in student.items():
    print(f"{key}: {value}")

# 七、列表套字典:一个班的学生(现实数据都长这样！)
students = [
    {"name":"dc","score":100},
    {"name":"lzy","score":200},
    {"name":"xy","score":300},
]

# 遍历每个学生,取名字和成绩
for s in students:
    print(f"{s['name']}: {s['score']}")

# 找出最高分
lowest = students[0]
for s in students:
    if s["score"] < lowest["score"]:
        lowest = s
print(f"最低分是{lowest['name']}:{lowest['score']}")

# 八、字典里也能装列表
meal = {
    "breakfast":["包子","豆浆"],
    "lunch":["米饭","红烧肉","青菜"],
}
print(meal["breakfast"])
print(meal["breakfast"][1])