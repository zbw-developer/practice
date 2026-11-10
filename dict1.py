student = {
    "name":"zbw",
    "age": 20,
    "city":"上海"
}

print(student["name"])
print(student["age"])
print(student["city"])
print(student["phone"])

student["age"] = 21
student["major"] ="计算机"
student["hobby"] = "打游戏"

print(student)
print(student.get("phone","未填"))