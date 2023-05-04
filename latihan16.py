contents = ["bisita", 
            "hari", 
            "damdam"]

isi = ["gajah.txt", "bakso.txt", "toko.txt"]

for contents, isi in zip(contents, isi):
    file = open(isi, 'w')
    file.write(contents)