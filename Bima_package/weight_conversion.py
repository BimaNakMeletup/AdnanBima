def weight_conversion():
    berat = int(input("Masukkan berat anda > "))
    satuan = input("Dalam apa berat yang anda masukkan? (K untuk KG, L untuk LBS) >")

    if satuan.lower() == 'l' :
        print(f"Berat anda dikonversi menjadi kilogram adalah {round(berat * 0.45392)} kg")
    elif satuan.lower() == 'k' :
        print(f"Berat anda dikonversi menjadi pons adalah {round(berat * 2.20462)} lbs")