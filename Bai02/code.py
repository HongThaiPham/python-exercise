x = int(input("Nhap so muon tinh: "))


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)


print("giai thua cua", x, "la", fact(x))
