lst=[1,2,3,4,1,2]
emp_lst=[]
[emp_lst.append(x) for x in lst if x not in emp_lst]
print(emp_lst)