def div():
    try:
        a=int(input('enter number:'))
        b=int(input('enter number:'))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print('cannot divide by zero')
    except ValueError:
        print('string input will not allowed')
div()
def add():
     e=int(input('enter number:')) 
     f=int(input('enter number:'))
     r=e+f
     print(r) 
add() 
        
