q=['1.what is the capital of india?',
'2.what is the national animal?']
ans=['delhi','tiger']
for x in range(len(q)):
   print(q[x])
   user_ans=input('enter answer:').lower()
   if user_ans == ans[x]:
      print('correct ans')
   else:
      print('wrong ans')   