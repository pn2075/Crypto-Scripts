
def square_multi(num,power, mod):
    result=1
    power= bin(power)
    for i in power[2:]:
        result=result**2
        if i =="1":
            result= result*num
        result= result%mod
    return result

print(square_multi(814886050799867001,73,179176752133705696))