def dec_to_bin(n):
    res = ""
    while n > 0:
        n, d = divmod(n, 2)
        digit = d + 0x30
        res = chr(digit) + res
    return "0b" + res

def dec_to_hex(n):
    res = ""
    while n > 0:
        n, d = divmod(n, 16)
        digit = d + 0x30 if d < 10 else d + 0x57
        res = chr(digit) + res
    return "0x" + res

number = int(input("Zadajte cislo: "))
while True:
    typ = input("1: Hexadecimalne\n2: Binarne\n")
    if typ == "1":
        print(dec_to_hex(number), hex(number))
        break
    elif typ == "2":
        print(dec_to_bin(number), bin(number))
        break
    else:
        print("Nespravna volba")
