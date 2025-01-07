a=[10,10,20]
for x in a:
    print(x,'-->',a.count(x))
print([a.count(x)for x in a])