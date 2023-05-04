nama_depan = input("silahkan masukan nama depan anda : ")
nama_belakang = input("silahkan masukan nama belakang anda : ")
nama_lengkap = [nama_depan.capitalize(), nama_belakang.capitalize()]
print(f"nama lengkap mu adalah : {nama_lengkap[0]} {nama_lengkap[1]}")
nama_dibalik = f"{nama_lengkap[1]} {nama_lengkap[0]}"
print(nama_dibalik)