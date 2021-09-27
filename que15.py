# 11 logon ka weight input le aur fir average weight print kare. 
# Aur fir yeh bhi check kare ki kya Average weight 5 ka multiple 
# (Yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi? 
# Note: Isme aapko input ka use karna padega. 
# Aap loop ke andar raw input ka use kar ke 11 baar raw_input le sakte ho.


i=1
sum=0
avg=0
while i<=11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    avg=sum%11
    i=i+1
    print("average of weight",avg)
    print("sum is",sum)
    if i%5==0:
        print(i,"it divisible by 5")
    else:
        print("it is not divisible by 5")

    

    


    



 






