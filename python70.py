import copy
lst1=[[10,20],[20,30]]
lst2=copy.copy(lst1)
lst1[1][0]=300
print(lst1)
print(lst2)
