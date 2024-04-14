o_sum=0
e_sum=0
p_sum=0

for i in range(10) : 
    x=int(input("please enter positive numbers :- ")) 
    if x <=0 : 
        x=int(input("error , positive only")) 
    p_flag=False
    for j in range (2,x) :
        if x ==1: 
            break
        else: 
            
            if x % j ==0 : 
                p_flag=True
    if p_flag :
        pass
    else:
        p_sum+=x
            

    if x%2==0 :
        e_sum+=x
    else:
        o_sum+=x
print("sum of odd" , o_sum)
print("sum of even" , e_sum) 
print("sum of prime" , p_sum)
print{}
hi
hjhjh3jkf
