print("makanan enak di Indonesia")
while True:
    user_action = input("ketik add untuk menambahkan, show untuk menampilkan makanan, edit untuk mengubah daftar makanan, complete untuk menghapus makanan yang sudah dimakan dan exit untuk keluar program: ")
    user_action = user_action.strip()

    if 'add' in user_action[0:5] or user_action.startswith('new'):
        makanan = user_action[4:] + "\n"
        
        with open('data.txt', 'r') as file:
            makanan_enak = file.readlines()
        
        makanan_enak.append(makanan)
        
        with open('data.txt', 'w') as file:
            file.writelines(makanan_enak)

    elif 'show' in user_action:   
        with open('data.txt', 'r') as file:
            makanan_enak=file.readlines()
        #makanan_enak = [item.strip('\n') for item in makanan_enak] <-- same as line 18-19
        
        print("ini daftar makanan yang enak :")
        for i, daftar in enumerate(makanan_enak):
            daftar = daftar.title()
            daftar = daftar.strip('\n')
            i = i + 1
            print(f"{i}. {daftar}")
        print(f"terdapat {len(makanan_enak)} makanan yang terdaftar")

    elif 'edit' in user_action:
        try:
            with open('data.txt', 'r') as file:
                makanan_enak = file.readlines()
            
            #file = open('data.txt', 'r')
            #makanan_enak = file.readlines()
            #file.close()
            
            number = int(user_action[5:]) - 1
            makanan_enak[number] = input("arep diganti panganan apa: ").capitalize() + '\n'
            with open('data.txt', 'w') as file:
                file = file.writelines(makanan_enak)

            #file = open('data.txt', 'w')
            #file.writelines(makanan_enak)
            #file.close()
            
            with open('data.txt', 'r') as file:
                makanan_enak = file.readlines()
            print("Oke manut, sekarang daftar makanan yang enak adalah :")
            for i, makanan in enumerate(makanan_enak):
                i = i + 1
                makanan = makanan.capitalize()
                makanan = makanan.strip('\n')
                print(f"{i}.{makanan}")
        except ValueError:
            print("Your command is invalid, please try again")
            continue
        except IndexError:
            print("there is no item in the number")
            continue
            
    elif 'complete' in user_action:
        try:
            number = int(user_action[9:]) - 1
            with open('data.txt', 'r') as file:
                makanan_enak = file.readlines()        
            remove_item = makanan_enak.pop(number)
            remove_item = remove_item.strip('\n') 
            print(f"makanan enak {remove_item.capitalize()} telah dihapus")
            
            with open('data.txt', 'w') as file:
                file = file.writelines(makanan_enak)
        except IndexError:
            print("there is no item in the number")
            continue            
    elif 'exit' in user_action:
            break
    else:
        print("salah input")
print("Yo wis")