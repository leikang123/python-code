class Res():

    def __init__(self,rname,rtype):
        
        
          self.rname = rname
          self.rtype = rtype

    def desr(self):
        print(self.rname.title() +" is name")
        print(self.rtype.title() +" is type")
          

    def open_res(self):
        print("餐馆正在营业") 
my_res = Res('leikang','siren')
her_res = Res('wangxiang','be')
his_res = Res('xcv','uy')
her_res.desr()
his_res.desr()
my_res.desr()
my_res.open_res()
