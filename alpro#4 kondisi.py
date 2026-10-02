makanan = ["ayam", "soto", "bakso",3]

#Lower untuk membaca semua tulisan menjadi kecil
masukan = input("cari menu: ").lower()

if masukan in makanan:
    print("menu tersedia" )

else:
    print("menu tidak tersedia")

    