import re
list = []
str = input("请输入：")
list = re.findall('\d+', str)
print(list)