def solution(n, b):
    def dec_to_base(num, base):  # covert decimal to number of arbitrary base
        base_num = ""
        while num > 0:
            dig = int(num % base)
            base_num += str(dig)
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
print(solution('1211', 10))
print(solution('2222', 3))
