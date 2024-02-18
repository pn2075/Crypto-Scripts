import square_multi
import re
from inverseMod import *
# q_129 = 32769132993266709549961988190834461413177642967992942539798288533
# p_129 = 3490529510847650949147849619903898133417764638493387843990820577
# totient = ((q_129 - 1) * (p_129 - 1))
# cipher_text = 91045328916998417442482698097341808065794629308863274299915006508648723904695483923175519319873972294295937946793571148693700025
# cipher_129 = 96869613754622061477140922254355882905759991124574319874695120930816298225145708356931476622883989628013391990551829945157815154
# n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541
dictionary = {
    "00": " ",
    "01": "a",
    "02": "b",
    "03": "c",
    "04": "d",
    "05": "e",
    "06": "f",
    "07": "g",
    "08": "h",
    "09": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "24": "x",
    "25": "y",
    "26": "z",
}


def inversemod(a, mod):
    m_original = mod
    y = 0
    x = 1
    if mod == 1:
        return 0
    while a > 1:
        quotient = a // mod
        t = mod
        mod = a % mod
        a = t
        t = y
        y = x - quotient * y
        x = t
        if x < 0:
            x += m_original
    return x


# print(square_multi.squar_multi(cipher_129,d,n))
# M = 112279045557353111466191264576338462748792786833448723340436268050278789671536070027619125194545156047711726992442487074922271120
# M_exam = 69909521861328319695629471809904219683738701366054595323320601641681047793154872354194734086314581782608014167527081712432037239


def translate(string):
    lst = re.findall('..?', string)

    return lst


# print(traslate(str(M_exam)))

def caculate_rsa(p, q, e, original):
    n = q * p
    c = square_multi.square_multi(original, e, n)
    return c


def backward_rsa(p, q, e, cipher):
    print("p:",p)
    print("q:",q)
    n = p * q
    print("N is ",n)
    totient_use = (p - 1) * (q - 1)
    print("totient:", totient_use)
    print(e)
    d_test = inverseMod(e, totient_use)
    print("d:", d_test)
    plain = square_multi.square_multi(cipher, d_test, n)
    return plain
p= 423284453
q= 423301049
e= 73
cipher = 8563992284203262
backward_rsa(p,q,e,cipher)

# test_txt = 200805001301070903002315180419000118050019172105011309190800151919090618010705
# print(caculate_rsa(3,11,7,5))
# print(backward_rsa(3,11,7,14))
# print(len(str((q_129))))
# print(d)
# print(cipher_129)
# print(cipher_text)
# print("Now")
# plain=backward_rsa(p_129, q_129, 9007, cipher_text)
# print(plain)
# print(caculate_rsa(p_129,q_129,9007,plain))

# lst = translate(str(backward_rsa(p_129, q_129, 9007, cipher_text)))
# print(caculate_rsa(p_129,q_129,9007,16051806211403201518250016192503081520080518011625))
# for i in lst:
#     print(dictionary[i], end="")

# print(backward_rsa(p_129, q_129, 9007, cipher_text))
# print(cipher_129 - test_txt)
