'''class Flipkart:
    #class att
    discount =10

    @classmethod
    def updateDiscount(cls,new_discount):
        cls.discount=new_discount

    @staticmethod
    def welcome():
        print('welcome to the flipkart')


    def myorders(self,order_id):
        #instance att
        self.order_id =order_id
        print(f"you have order these proudct with the id{self,order_id}")
        
#claass att ,class meth,ints att ,ints meth,static=>objrct
#class att, class metth, stsaic=> class
anju =Flipkart()
himaja=Flipkart()

print(anju.discount)
print(Flipkart.discount)

anju.myorders(1)
print(anju.order_id)

anju.updateDiscount(20)
anju.myorders(2)
anju.welcome()

Flipkart.updatediscount(20)
flipkart.welcome()
'''
'''
class instagram:
    def _init_(self,username,password):#init is constucter
        self.username=username
        self.password=password
        self.posts=[]
        
    @property
    def myposts(self):
        return self.posts
    
    @myposts.setter
    def myposts(self,postname):
        self.posts.append(postname)
        

    def get_password(self):
        return self.password
    
    def set_password(self,new_password):
        self.password=new_password
        
        
        print(f"hello{self.username},welcome to the instagram")
anju = instagram ('venkatteeja','venkat12@')

print("before updating :",anju.username)
anju.username ="himaja"
print("after  updating : ",anju.username)


print("befor updating :",anju.get_password())
anju.set_password('venkat teja12@')
print("after updating: ",anju.get_password())

print(anju.myposts)
anju.myposts ='sunset.png'
anju.myposts='beach.mp4'
print(anju.myposts)
'''
'''
#book problem
class book:
    def _init_(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print(f"title: {self.title},author :{self.author},price: ${self.price}")

book1 =book("clean code " ,"robert bownerry",4776)
book1.display_info()
'''
'''
#empolyee problem
class employee:
    def _init_ (self,name,base_salary):
        self.name = name
        self.base_salary = base_salary


    def display_info(self):
        print(f"name: {self.name},base_salary: {self.base_salary} is the info")
        
employee1 = employee("venaktteja",50000)
employee1.display_info()
'''
#oops concept
'''
class instagramV1:
    def reel(self):
        print("you can post the reel")
class instagramV2(instagramV1):
    def story(self):
        print("you can  upload a story")
class instagramV3(instagramV2):
    def note(self):
        print("you can upload your thought")
class meta(instagramV3):
    def ai(self):
        print("you can use the ai")
class crossplatform(instagramV3):
    def integrating(self):
        print("you can integrate with whatsapp and facebook")

print('anju - instgramV1')
anju = instagramV1()
anju.reel()
        

print('himaj-instagramV2')
himaja =instagramV2()
himaja.reel()
himaja.story()

print('sanjusha-instagramV3')
sanjusha= instagramV3()
sanjusha.reel()
sanjusha.story()
sanjusha.note()
'''
#inheritence
'''
class A:
class B(A):


class A:
class B(A):
class C(B):


class A:
class B:
class C:
class D(A,B,C):

class A:
class B(A):
class C(A):
'''
class whatsappV0:
    def status(self):
        print("you can upload image and videos")

class whatsappV1:
    def status(self):
        print("you can like, react and reply")

class whatsappV2(whatsappV0,whatsappV1):
    def status(self):
        whatsappV0.status(self)
        whatsappV1.status(self)
        
        print("you can add music and filters also")

anju = whatsappV2()
anju.status()
