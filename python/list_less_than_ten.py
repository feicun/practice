a = []
a.append(1)
a.append(5)
a.append(6)
a.append(12)
a.append(19)
a.append(21)

num = int(raw_input("Choose a number: "))
new_list = []
for i in a:
    if i < num:
        new_list.append(i)
print new_list
