# 第 7 课:学生成绩管理系统 v1.0
# 数据形状:字典套字典 —— 名字当键,信息当值
#   students = {"dc": {"score": 88}, "lzy": {"score": 55}}

students = {}

# ═══════ 功能函数:先搭空架子,后面一个一个填 ═══════

def add_student():
    name = input("请输入学生姓名:").strip()        # .strip() 去掉首尾多余空格

    # 1\名字不能为空
    if name == "":
        print("姓名不能为空!")
        return
    # 2\重名检查 —— 名字已经是字典的键了吗?
    if name in students:
        print(f"学生{name}已存在,不能重复添加!")
        return
    # 3\分数:输入 + 检查是不是合法数字
    try:
        score = int(input(f"请输入{name}分数(0-100): "))
    except ValueError:
        print("分数必须是数字!")
        return
    # 4\分数范围检查(Python特有的链式比较)
    if not (0 <= score <= 100):
        print("分数必须在 0-100 之间!")
        return
    # 5\检查全部通过,存进字典
    students[name] = {"score": score}
    print(f"已添加:{name},分数:{score}")


def show_all():
    if not students:
        print("暂无学生记录!")        # 空字典在Python等于"假"
        return
    print(f"\n共{len(students)}名学生:")
    print("-"*30)
    for name, info in students.items():
        print(f"{name}:{info['score']}分")
    print("-"*30)
def find_student():
    name = input("请输入要查找的姓名:").strip()

    info = students.get(name)
    if info is None:
        print(f"没有找到学生:{name}")
        return

    print(f"{name}的分数是:{info['score']}")

def delete_student():
    name = input("请输入要删除的姓名:").strip()
    info = students.pop(name,None)
    if info is None:
        print(f"没有找到学生:{name}")
        return

    print(f"已删除学生:{name}(原分数 {info['score']})")

def statistics():
    if not students:
        print("暂无学生记录,无法统计!")
        return

    scores = [info["score"] for info in students.values()]

    pass_count = len([s for s in scores if s >= 60])

    print("\n====== 统计分析 ======")
    print(f"学生总数:{len(scores)}人")
    print(f"平均分:{sum(scores)/len(scores):.2f}")
    print(f"最高分:{max(scores)}")
    print(f"最低分:{min(scores)}")
    print(f"及格人数:{pass_count}人(及格率{pass_count / len(scores) * 100:.1f}%)")

# ═══════ 主函数:显示菜单 + 循环 + 派活 ═══════

def main():
    while True:
        print("\n====== 学生成绩管理系统 ======")
        print("1. 添加学生")
        print("2. 查找所有学生")
        print("3. 查找学生")
        print("4. 删除学生")
        print("5. 统计分析")
        print("6. 退出")

        choice = input("请选择(1-6):")     # 收指令

        if choice == "1":                 # 派活:按数字叫对应的函数
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            find_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            statistics()
        elif choice == "6":
            print(f"再见!")
            break                         # ★ 跳出循环 = 结束程序
        else:
            print("无效输入,请输入 1-6")


if __name__ == "__main__":                                # ★ 程序入口:从这一行开始跑
    main()