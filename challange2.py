while True:
    num = int(input("Masukkan bilangan: "))

    if (10 < num < 15) or (20 < num < 25) or (35 < num < 40):
        print("Benar")
        break
    else:
        print("Salah, coba kembali !")