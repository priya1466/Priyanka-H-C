lst=[1,2,3,4,1,2]
emp_lst=[]
dupl_lst=[]
for x in lst:
    if x in emp_lst:
        dupl_lst.append(x)
    else:
        emp_lst.append(x)
print(dupl_lst)