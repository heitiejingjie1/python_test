"""
bytes
"""

name = "殷浩"
gname = name.encode("gbk")  # 编码
print(gname)
uname = name.encode("utf-8")
print(uname)

"""字节转换"""
dgname = gname.decode("gbk")  # 解码
print(dgname)
uname = dgname.encode()
print(uname.decode())
