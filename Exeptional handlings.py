'''try:
    #print(b)
    l=[1,23]
    #print(1[7])
    d={1:2,3:2,4:5}
    #print(d[9])
    #a=int(input("enter the integer:"))
    #print(10/0)
    #print('a'+10)

except (TypeError,ZeroDivisionError,KeyError,IndexError,ValueError)as e:
    print("Error occured:",e)

else:
    print("a=",a)

finally:
    print("End of the program")
'''
'''
try:
    balance=1000
    amount=-10
    if amount<0:
        raise Exception('amount needs to be postive')
    balance+= amount

except Exception as e:
    print("error occured:",e)
else:
    print("current balance:",balance)
finally:
    print("end of the program")
'''
