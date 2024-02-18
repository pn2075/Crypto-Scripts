def inverseMod(number, mod):
    m_original = mod
    y = 0
    x = 1
    if mod == 1:
        return 0
    while number > 1:
        quotient = number // mod
        t = mod
        mod = number % mod
        number = t
        t = y
        y = x - quotient * y
        x = t
        if x < 0:
            x += m_original
    return x

print(inverseMod(3,5))