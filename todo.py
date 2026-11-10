import json
import os

FILE = "todos.json"


def load_todos():
    """从文件读取;文件不存在就返回空列表"""
    if not os.path.exists(FILE):
        return[]
    with open(FILE,"r",encoding="utf-8")as f:
        return json.load(f)


def save_todos(data):
    """把数据写回文件"""
    with open(FILE,"w",encoding="utf-8")as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

todos = load_todos()

while True:
    command = input("命令(add / list / done / del / quit):")

    if command =="add":
        task = input("要添加什么?")
        todos.append({"task": task,"done": False})
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

    elif command =="done":
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

    elif command == "del":
        num  = input("要删除第几条")
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

    elif command =="quit":
        print("再见")
        break

    else:
        print(f"还不支持:{command}")

        