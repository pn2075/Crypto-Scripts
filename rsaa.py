import square_multi
import math
import random
SECURITY_INT=15
def euclid(a,b):
    while b:
        a,b=b, a%b
    return a
def check_prime(n):
    if n==2:
        return True
    elif n%2 ==0 or n<=1:
        return False
    stop_point= int(math.sqrt(n))+1
    for prime_test in range(3,stop_point,2):
        if n%prime_test==0:
            return False
    return True
#print(squar_multi(30,11,31))
#print(squar_multi(3,30,31))
def find_order(num, mod):
    lst=[]
    order=0
    for i in range(mod-1):
        lst.append(squar_multi(num,i,mod))
        order+=1
    print(order)
    return lst
find_order(3,53)
def fermat_test(n,times):
    if n==2 or n ==3:
        return True
    elif n%2==0 or n<=1:
        return False
    else:
        for _ in range(times):
            a = random.randint(2, n-1)
            while euclid(a,n)!=1:
                a = random.randint(2, n-1)

            if square_multi.square_multi(a,n-1,n)!=1:
                return False
        return True

def check_last_3_from_n(n):
    n-=1
    return_list=[]
    while len(return_list)<3:
        if fermat_test(n,SECURITY_INT)==True:
            if not check_prime(n):
                return_list.append(n)
        n-=1
        if n==0:
            break
    return return_list
#print(fermat_test(561,2))
print(check_last_3_from_n(10**6)) #[997633, 852841, 838201]
print(check_last_3_from_n(10**7)) #[9613297, 9439201, 8719309]
