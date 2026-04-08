print("---- MENU ----")
print("index  product  price")
print("------------------------")

print("1 milk  -       30")
print("2 sugar -       50")
print("3 soap  -       40")
print("4 bread -       35")
print("5 tea powder -  90")
print("6 cooking oil -130")
print("7 salt -        20")
print("8 rice -        60")
print("9 eggs (12p) -  70")
print("10 books")
print("-------------------------")


products = ['rice','sugar','wheat flour','milk','eggs','cooking oil','tea powder','salt,'bread','soap']

prices = [60,30,40,20,70,80,110,35,45,65]

print("------welcome to grocery store ------")
print("here are the available products:/n")

print('index'.ljust(6,' '),'products[i].ljust(15,' '),'price'.ljust(6,' ')

for i in range(10):
      print(str(i=1).ljust(6,' '),products[i].ljust(15,' '),str(prices[i]).ljust(6,' '))

items = list(map(int,input("enter the indexes: ").split()))

      
print("selected item: ")
total_amount = 0
for item in items:
      print(products[items-1],prices[item-1])
      total_amount+= prices[items-1]
    thank you for shopping with us


      
