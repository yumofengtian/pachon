import re
list = ['']
str = input("请输入：")
list1 = re.findall('\d{11}',str)
list2 = re.findall('[\d@163.com]+',str)
list2 = re.findall('[\d@qq.com]+',str)
for el in list2:
    if el.endswith('m'):
        list.append(el)
list.remove('')
list1 = set(list1)
print(list1)
print(list)
