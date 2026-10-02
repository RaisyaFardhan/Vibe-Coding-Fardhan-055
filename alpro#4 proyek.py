import time 

List_resep = ("telur","gula", "tepung", "garam", "mentega", "coklat")
score = 0

print("hai, kamu harus tebak 3 resep kue kering, siap?")
time.sleep(3)

resep1 = input("resep 1").lower()
if resep1 in List_resep:
    print("Selamat!!! kamu berhasil menebak " + resep1)
    score += 1
else :
    print("Maaf, tebakan kamu salah")

resep2 = input("resep 2").lower()
if resep2 in List_resep:
    print("Selamat!!! kamu berhasil menebak " + resep2)
    score += 1
else :
    print("Maaf, tebakan kamu salah")

resep3 = input("resep 3").lower()
if resep3 in List_resep:
    print("Selamat!!! kamu berhasil menebak " + resep3)
    score += 1
else :
    print("Maaf, tebakan kamu salah")

print(" game berakhir, kamu memiliki " +  str(score)  +  " point ")
print(List_resep)