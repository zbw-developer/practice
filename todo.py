import json
import os

FILE = "todos.json"


def load_todos():
    """从文件读取;文件不存在就返回空列表"""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8")as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("todos.json 格式有问题问，先当作空清单处理")
        return []


def save_todos(data):
    """把数据写回文件"""
    with open(FILE, "w", encoding="utf-8")as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


todos = load_todos()

while True:
    command = input(
        "命令(add / list / done / del / stat / clear / resrt / quit):")

    if command == "add":
        task = input("要添加什么?")
        todos.append({"task": task, "done": False})
        print(f"已添加:{task}")
        save_todos(todos)

    elif command == "list":
        if len(todos) == 0:
            print("清单是空的，先 add 一条")
        else:
            print("===== 待办清单 =====")
            i = 1
            for item in todos:
                if item["done"]:
                    mark = "✔"
                else:
                    mark = " "
                print(f"{i}. {item['task']}  {mark}")
                i = i + 1
            print("====================")

    elif command == "done":
        num = input("要标记第几条?")
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(todos):
                todos[index]["done"] = True
                print(f"已完成:{todos[index]['task']}")
                save_todos(todos)
            else:
                print("没有这条编号")
        else:
            print("请输入数字")

    elif command == "stat":
        total = len(todos)
        done = 0
        for item in todos:
            if item["done"]:
                done = done + 1
        print("===== 统计 =====")
        print(f"总共 {total} 条")
        print(f"已完成 {done} 条")
        print(f"未完成 {total - done} 条")
        print("================")

    elif command == "del":
        num = input("要删除第几条")
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(todos):
                removed = todos.pop(index)
                print(f"已删除:{removed['task']}")
                save_todos(todos)
            else:
                print("没有这条编号")
        else:
            print("请输入数字")

    elif command == "clear":
        kept = []
        for item in todos:
            if not item["done"]:
                kept.append(item)
        removed = len(todos) - len(kept)
        todos = kept
        save_todos(todos)
        print(f"已清空 {removed} 条已完成")

    elif command == "reset":
        confirm = input("确认要清空全部吗? (y/n)")
        if confirm.lower() == "y":
            todos = []
            save_todos(todos)
            print("已清空全部")
        else:
            print("已取消")

    elif command == "quit":
        print("再见")
        break

    else:
        print(f"还不支持:{command}")
