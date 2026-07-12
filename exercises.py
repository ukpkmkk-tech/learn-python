 # 个人信息名片
print("======个人信息名片======")
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
city = str(input("请输入你所在的城市："))
print(f"你好!{name},你的年龄是{age},你所在的城市为：{city}")

 # 温度转换器
print("\n======温度转换器======")
celsius = float(input("你好!我是温度转换助手,你可以告诉我今天的气温(摄氏度℃),我帮你转换："))
fahrenheit = (celsius * 9 / 5) + 32
print(f"转换完成,今天的华氏度温度为:{fahrenheit:.1f}℉")

 # BMI计算器
print("\n======BMI计算器======")
height = float(input("请输入你的身高(m):"))
weight = float(input("请输入你的体重(kg):"))
bmi = weight / (height ** 2)
print(f"你的 BMI 是：{bmi:.2f}")