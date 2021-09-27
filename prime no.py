# Prime numbers woh numbers hote hai jo sirf 1 aur apne aap se divisible hote hain. 
# Jaise 1. 13 prime hai kyunki 13 sirf 13 aur 1 se perfectly divide hota hai.
# Aur kisi bhi number se perfectly divide nahi hota.
# 2. 4 prime nahi hai kyunki 4 apne aap se aur 2 aur 1 se perfectly divide hota hai.

# Prime number ke liye aapko check karna hoga ki woh number kaun kaun se numbers se divisible hai.
# Yeh loop chala ke kar sakte ho.



# num=1
# i=2
# while i<=100: 
#     count=0
#     while num %i==0:
#         count=count+1
#         break
#     i=i+1
#     if count==2:
#         print("prime")
#     else:
#         print("not prime")
    

# num = 1
# while(num <= 100):
#     count = 0
#     i = 2
#     while(i <= num//2):
#         if(num % i == 0):
#             count = count + 1
#             break
#         i = i + 1
#     if (count == 0 and num!= 1):
#         print(" %d" %num, end = '  ')
#     num = num + 1


# num=1
# while num <=100:
#     count = 0



i=1
while i<=100:
    if i%1!=0 or i%2!=0:
        print(i)
    i=i+1





