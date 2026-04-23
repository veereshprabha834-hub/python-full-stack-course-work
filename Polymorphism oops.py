
'''#po

same method
differ

1-method overloading - same method ,different parameters,same/diff classes
2-method overridding - same method ,same parameters
'''
'''
class hotstar:
    def __init__(self,username):
        print("Hi{username}!\nwelcome to the hotstar!!!!")
    def promo(self):
        print("you can watch the promos")
    def login(self):
        print("you can login to the hotstar")
    def search(self):
        print("you can search the movies")
    def profile(self):
        print("you can edit your profile")
    def videocontrollers(self):
        print("you can pause and play")
    def suggestions(self):
        print("you can check out the suggestions")
    def movie(self):
        print("you have access for old movies")
    def ads(self):
        print("ads will be run")
    def download(self):
        print("you can download the movies")
    def quality(self):
        print("you can watch the movies in low quality")
        
class premiumhotstar:
    def __init__(self,username):
        print(f"Hi {username}!\nwelcome to the premiumhotstar!!!!")
    def movie(self):
        print("you have access for all the movies")
    def ads(self):
        print("ads won't be run")
    def download(self):
        print("you can download the movie")
    def quality(self):
        print("you can watch movie with high quality")


veeresh = hotstar('veeresh')
veeresh.promo()
veeresh.login()
veeresh.search()
veeresh.profile()
veeresh.videocontrollers()
veeresh.suggestions()
veeresh.movie()
veeresh.ads()
veeresh.download()
veeresh.quality()

print('\n')

prabha = premiumhotstar('prabha')
prabha.movie()
prabha.ads()
prabha.download()
prabha.quality()
'''
class num:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
    def __mul__(self,other):
        return self.num*other.num
    def __gt__(self,other):
        return self.num>other.num
    def __it__(self,other):
        return self.num<other.num
    def __str__(self):
        return str(self.num)

a = num(10)
b = num(20)
print(a+b)
print(a-b)
print(a*b)
print(a>b)
print(a<b)
print(a,b)

