val=[1,87,79]
for x in range(len(val)):
    for y in range(len(val)):
        if val[x]<val[y]:
            val[x],val[y]=val[y],val[x]
        else:
            val[x],val[y]=val[x],val[y]
print(val)