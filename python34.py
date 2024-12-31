tkts=[1,2,3,4,5]
print('avilable tkts',tkts)
user_input=int(input('enter how many tkts u wanna buy'))
for x in range(user_input):
    tkts_num=int(input('enter tctk number'))
    tkts.remove(tkts_num)
    print('avilable tkts',tkts)