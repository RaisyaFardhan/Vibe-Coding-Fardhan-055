country = input("dimana kamu mau berkendara?")
usia = int(input("berapa usia kamu?"))

if country == "afrika selatan":
    if usia >= 18:
        print("kamu boleh berkendara")
    else:
        print("kamu belum boleh berkendara")    

elif country == "meksiko":
    if usia >= 18:
        print("kamu boleh berkendara")
    elif usia >= 16:
        print("kamu boleh berkendara dengan parental agreement")
    elif usia >= 15:
        print("kamu boleh berkendara dengan parental supervision")
    else:
        print("kamu belum boleh berkendara")

elif country == "india":
    if usia >= 18:
            print("kamu boleh berkendara")
    else: 
            print("kamu belum boleh berkendara") 

elif country == "prancis":
    if usia >= 18:
            print("kamu boleh berkendara")
    elif usia >= 15:
            print("kamu boleh berkendara dengan parental supervision")
    else:
            print("kamu belum boleh berkendara")



            