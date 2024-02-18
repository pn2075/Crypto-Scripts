AES_poly_hex = int("0x11b", 16)


def multi_2_hex(hex1, hex2):
    doub_list = []
    double_num = int(hex1, 16)
    sum = double_num
    half_num = int(hex2, 16)
    print(sum)
    if half_num % 2 == 0:
        sum = 0
    while half_num != 1:
        double_num = double_num << 1
        if double_num > int("FF", 16):
            double_num = double_num ^ AES_poly_hex
        half_num = half_num >> 1
        if half_num % 2 == 1:
            sum = sum ^ double_num

        doub_list.append((hex(double_num), half_num))
    print(doub_list)
    return hex(sum)


