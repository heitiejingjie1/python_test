import os

"""修改文件"""

with (
    open("name.txt", mode="r", encoding="utf-8") as f1,
    open("name_副本.txt", mode="w", encoding="utf-8") as f2,
):
    for line in f1:
        line = line.strip()
        if line.startswith("殷"):
            line = line.replace("殷", "胡")
        f2.write(line)
        f2.write("\n")


"""删除源文件"""
os.remove("name.txt")
"""重命名副本文件"""
os.rename("name_副本.txt", "name.txt")
