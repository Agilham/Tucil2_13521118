# fungsi validasi input nilai n adalah integer
def getInteger():
    while True:
        try:
            n = int(input("Masukkan nilai n: "))       
        except (ValueError):
            print("Input nilai n bukan integer. Ulangi input nilai n!")
            continue
        else:
            break
    return n

# fungsi validasi input nilai n >= 2
def getValid():
    n = getInteger()
    while (n < 2):
        print("Input nilai (n < 2). Ulangi input nilai n!")
        n = getInteger()
    return n
