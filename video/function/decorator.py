"""
装饰器：
     本质是一个闭包
     在目标函数前后插入一些操作
自己推导一下装饰器的过程
"""

LOGIN_FLAG = False


def wrapper(fn):
    def inner(*args, **kwargs):
        global LOGIN_FLAG

        if not LOGIN_FLAG:
            while 1:
                print("你还未登录。。。")
                user = input(">>>")
                password = input(">>>")
                if user == "admin" and password == "123":
                    print("登录成功")
                    LOGIN_FLAG = True
                    break
                else:
                    print("用户名或密码输入错误")

        ret = fn(*args, **kwargs)
        return ret

    return inner


@wrapper
def add():
    print("添加员工信息")


@wrapper
def delete():
    print("删除员工信息")


@wrapper
def update():
    print("更新员工信息")


@wrapper
def search():
    print("查询员工信息")


add()
delete()
update()
search()
