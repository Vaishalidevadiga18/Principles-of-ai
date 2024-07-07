
list = [12,2,3,9,3,2,99,12]
print("The original list is : " + str(list))

res = []
for i in list:
    if i not in res:
        res.append(i)
print("The list after removing duplicates : " + str(res))
