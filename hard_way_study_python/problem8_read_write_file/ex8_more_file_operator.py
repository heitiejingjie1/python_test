from sys import argv
from os.path import exists

"""解包命令行参数"""
scripts, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

"""打开待复制文件"""
in_file = open(from_file)
"""读取文件数据"""
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Reday. hit RETURN to continue, CTRL-C to abort.")

input()

"""打开待写入文件"""
out_file = open(to_file, "w")
"""写入文件"""
out_file.write(indata)
print("Alright. all done.")

"""关闭文件"""
out_file.close()
in_file.close()
