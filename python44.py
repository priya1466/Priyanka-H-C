q=['1.what is the capital of india?',
'2.what is the national animal?']
ans=['delhi','tiger']
for x in q:
   print(x)
   user_ans=input('enter answer:')
   if user_ans in ans:
      print('correct ans')
   else:
      print('wrong ans')   
