import square_multi as sm
def euclid(a,b):
    while b:
        a,b=b, a%b
    return a

def find_generator_biggerthan(a_field,num_from,count):
    check_with= a_field-1
    for i in range(num_from,check_with-1):
        if euclid(i+1,check_with)==1:
            count -=1
            print(i)

        if count==0:
            return i
def generators(min_a, n):
    """Find generators in the set Z*[n] (starting from the first generator greater than min_a)"""

    z = {x for x in range(n) if euclid(x, n) == 1}
    for a in range(min_a, n):
        if {pow(a, p) % n for p in range(1, len(z) + 1)} == z:
            yield a


if __name__ == '__main__':
    print(next(generators(1009, 4969)))
