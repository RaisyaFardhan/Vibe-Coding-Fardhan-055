available_pizzas = ["margherita" , "calzone", "four chese", "peperoni", "napoli"]
pizza_order = []
total_price = 0
print ("halo, dibawah ini merupakan menu toko ini")
for i, pizza in enumerate(available_pizzas) :
    print(str(i) + ". " + pizza )
continue_ordering = True
while continue_ordering:
    answer = input("apakah kamu ingin membeli pizza(y/t)?")
    if answer == "y" :
        valid_pizza_choice = False

        while not valid_pizza_choice:
            pizza_choice = int(input("pizza apa yang anda inginkan?"))

            #validate user input
            if (pizza_choice >= 0) and \
            (pizza_choice <= len(available_pizzas) - 1):
                pizza_order.append(available_pizzas[pizza_choice])
                print("menambahkan " + available_pizzas[pizza_choice] + " pizza kesalam pesanan")
                total_price += 10
                valid_pizza_choice = True

            else:
                print("tolong masukan angka yang tertera dalam menu")
    else:
        continue_ordering = False
print("kamu memeasan: ")
print(pizza_order)
print("kamu harus membayar " + str(total_price) + " rupiah. ")

tip = 0.0
valid_tip = False 
while not valid_tip:
    tip = float(input("berapa tip yang ingin ditinggalkan(0-25%)?"))
    if (tip >= 0) and (tip <= 25):
        valid_tip = True

    else:
        print("tolong masukan angka antara 0-25.")

total_price += total_price *tip/100
print("Terima kasih! Total harga " + str(total_price) + " rupiah. pizza otw!")
