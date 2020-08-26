# def base_to_dec(num_str,base):
#     num_str = num_str[::-1]
#     num = 0
#     for k in range(len(num_str)):
#         dig = num_str[k]
#         if dig.isdigit():
#             dig = int(dig)
#         else:    #Assuming its either number or alphabet only
#             dig = ord(dig.upper())-ord('A')+10
#         num += dig*(base**k)
#     return num

def solution(n, b):
    def dec_to_base(num,base):
        base_num = ""
        while num>0:
            dig = int(num%base)
            if dig<10:
                base_num += str(dig)
            else:
                base_num += chr(ord('A')+dig-10)
            num //= base

        base_num = base_num[::-1]
        return base_num

    minion_IDs = []
    minion_ID = str(n)
    while minion_ID not in minion_IDs:
        minion_IDs.append(minion_ID)
        x = ''.join(sorted(minion_ID)[::-1])
        y = ''.join(sorted(minion_ID))
        int_z = int(x, b) - int(y, b)
        z = dec_to_base(int_z, b)
        minion_ID = (len(str(n)) - len(z)) * '0' + z

    return (len(minion_IDs) - minion_IDs.index(minion_ID))

print(solution('210022', 3))
# print((4-3)*'0' + dec_to_base(999, 10))
