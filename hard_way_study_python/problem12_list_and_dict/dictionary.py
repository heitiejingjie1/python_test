"""省份简称"""

provinces = {
    "ChongQing": "CQ",
    "HuBei": "HB",
    "HuNan": "HN",
    "GuiZhou": "GZ",
    "SiChuan": "SC",
}


"""城市所属省份"""
cities = {
    "CQ": "ChongQing",
    "SC": "ChengDu",
    "HN": "ChangSha",
}

"""添加另外的一些城市"""
cities["HB"] = "WuHan"
cities["GZ"] = "YunNan"

"""打印城市"""
print("-" * 10)
print("HB省包含: ", cities["HB"])
print("GZ省包含: ", cities["GZ"])

"""打印省份"""
print("-" * 10)
print("ChongQing简称为: ", provinces["ChongQing"])
print("SiChuan简称为: ", provinces["SiChuan"])

"""使用省份和城市组合来打印城市"""
print("-" * 10)
print("GuiZhou省包含: ", cities[provinces["GuiZhou"]])
print("HuBei省包含: ", cities[provinces["HuBei"]])

"""打印所有省份简称"""
print("-" * 10)
for provin, abbrev in list(provinces.items()):
    print(f"{provin} 简称为 {abbrev}.")

"""打印城市所属省份"""
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{city} 所属省份为 {abbrev}.")

"""现在把两者结合"""
print("-" * 10)
for provin, abbrev in list(provinces.items()):
    print(f"{provin} 简称为 {abbrev}.")
    print(f"城市为 {cities[abbrev]}")
print("-" * 10)

"""通过某种方式安全地获取某个可能不存在的缩写形式"""
provin = provinces.get("FuJian")
if not provin:
    print("Sorry, no FuJian.")

"""通过默认值获取城市"""
city = cities.get("TX", "Does Not Exist")
print(f"这城市所属省份'TX': {city}")
