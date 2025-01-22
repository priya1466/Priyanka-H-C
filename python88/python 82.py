class insta:
    def __inti__(self):
        self.version=13.13
        self.developer='raj'
    def auth(self):
        user_name=input('enter user name')
        password=input('enter password')
        if user_name=='prince123' and password='123':
           print('scussful')
        else:
            print('login failed')
im=insta()
im.auth()
