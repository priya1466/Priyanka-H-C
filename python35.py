lst=[1,2,3,4,1,2]
emp_lst=[]
for x in lst:
    if x not in lst:
        emp_lst.append(x)
print(emp_lst)