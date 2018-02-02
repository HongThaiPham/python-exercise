# Câu hỏi:

# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance

# Gợi ý:

# Khi định nghĩa tham số instance, cần thêm nó vào __init__
# Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.


class Person:
    name = "Leo"

    def __init__(seft, name=None):
        seft.name = name


Thai = Person("Thai")
print("%s name is %s" % (Person.name, Thai.name))

Bob = Person()
Bob.name = "Bob"
print("%s name is %s" % (Person.name, Bob.name))
