from  square_multi import *
def find_discrete_log(num,mod,destination):
    a_set= set()
    for i in range(mod-1):
        mod_result= squar_multi(num,i,mod)
        a_set.add(mod_result)
        print(num,"^",i, "mod",mod,":", mod_result)
        if mod_result==destination:
            return i
    print(len(a_set))
    return "Not found"

print(find_discrete_log(3,31,13))
def inversemod(a,mod):
    m_original= mod
    y=0
    x=1
    if mod==1:
        return 0
    while a>1:
        quotient= a//mod
        t= mod
        mod= a%mod
        a=t
        t=y
        y= x-quotient*y
        x=t
        if x<0:
            x+= m_original
    return x
print(inversemod(30,31))