tanggal = int(input("tanggal : "))
bulan = input("bulan : ").capitalize()
tahun = int(input("tahun : "))
jam = int(input("jam : "))
journal = input("apa yang telah anda lakukan : \n")

with open(f"Jam {jam}.00 - {tanggal} - {bulan} - {tahun}.txt", 'w') as file:
    file.write(journal)