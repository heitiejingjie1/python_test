"""复杂输出格式"""

"""格式化字符串字面值"""
year = 2025
event = "modify file"
print(f"Return of the {year} {event}")

yes_votes = 42572654
total_votes = 85705175
percentage = yes_votes / total_votes
print("{:-9} yes votes {:2.2%}".format(yes_votes, percentage))
