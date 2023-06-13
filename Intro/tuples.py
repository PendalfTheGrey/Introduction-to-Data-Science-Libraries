#temporary data storage
item = ("Healthkit", 4, True,"Healthkit")
item_2 = ("Knife",6)
print(item[0])
#does not work since it is immutable
#item[1] = 10
print(item)
print(item_2)

#work in lists
print(item.count("Healthkit"))
print(item.index("Healthkit"))