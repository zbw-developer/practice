import json
import os
from rich import print
from rich.table import Table

FILE = "todos.json"

def load_todos():
    """从文件读，文件不存在返回"""
    if not os.path.exists(FILE):
        return[]
    try:
        with open(FILE, "r", encoding= "utf-8")as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("todos.json格式有问题,开新列表")
        return[]

def save_todos(data):
    with open(FILE, "w", encoding= "utf-8")as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

todos = load_todos()

while True:
    command = input("命令(add/list/done/del/stat/clear/reset/search/edit/quit)")

    if command == "add":
        task = input("需要添加什么:")
        pr = input("优先级(高/中/低,直接回车=中):")
        if pr == "":
            pr = "中"
        todos.append({"task":task,"done":False,"priority":pr})
        print(f"已添加:{task}")
        save_todos(todos)

    elif command == "list":
        if len(todos) == 0:
            print("清单是空的,先add一条")
        else: 
            print("[bold cyan]=== 待办清单 ===[/bold cyan]")
            i = 1
            for item in todos:
                mark = "✓" if item["done"] else " "
                p = item.get("priority","中")

                if p == "高":
                    color = "red"
                elif p == "低":
                    color = "green"
                else:
                    color = "yellow"

                print(f"{i}. {item['task']} {mark}[{color}]{p}[/{color}]")
                i = i + 1
            print("=" * 20)

    elif command == "done":
        num = input("要标记第几条?")
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(todos):
                todos[index]["done"] = True
                save_todos(todos)
                print(f"已完成: {todos[index]['task']}")
            else:
                print("没有这条编号")
        else:
            print("请输入数字")

    elif command == "del":
        num = input("要删第几条?")
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(todos):
                removed = todos.pop(index)
                save_todos(todos)
                print(f"已删除{removed['task']}")
            else:
                print("[red]没有这条编号[/red]")
        else:
            print("[red]请输入数字[/red]")

    elif command == "stat":
        total = len(todos)
        done = 0
        for item in todos:
            if item["done"]:
                done = done + 1

        table = Table(title="统计")
        table.add_column("项目")
        table.add_column("数量", justify="right")
        table.add_row("总共", str(total))
        table.add_row("已完成", str(done))
        table.add_row("未完成", str(total - done))
        print(table)

    elif command == "clear":
        kept = []
        for item in todos:
            if not item["done"]:
                kept.append(item)
        removed = len(todos) - len(kept)
        todos = kept
        save_todos(todos)
        print(f"已清理{removed}条已完成")

    elif command =="reset":
        confirm = input("确认要清空全部吗? (y/n)")
        if confirm.lower() == "y":
            todos = []
            save_todos(todos)
            print("已清空全部")
        else:
            print("已取消")

    elif command == "search":
        keyword = input("搜什么")
        found = 0
        for item in todos:
            if keyword in item["task"]:
                print(f"- {item['task']}")
                found = found + 1
        if found == 0:
            print("没找到")

    elif command == "edit":
        num = input("要标记第几条?")
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(todos):
                new_task = input("新的内容?")
                todos[index]["task"] = new_task
                save_todos(todos)
                print(f"已修改: {new_task}")
            else:
                print("改第几条")
        else:
            print("请输入数字")

    elif command == "quit":
        print("再见")
        break
