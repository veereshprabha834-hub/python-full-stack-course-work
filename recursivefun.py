def fun():
    if base_con:
        return
    fun()

    

def display(l,i,sum):
    if i==len(l):
        return sum
   return display(l,i+1,sum+1[i])
            
    
print(display([1,2,3,4,5,6,7,8,9],0))




    
