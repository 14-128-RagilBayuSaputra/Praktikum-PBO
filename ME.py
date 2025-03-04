Nama = input("Masukkan nama: ")
nim = int(input("Masukkan nim: "))
kata_kata = input("Apa yang kamu inginkan pada tahun ini: ")

nama_file = "Me.txt"

with open(nama_file, 'w') as f:
    f.write(f"Nama: {Nama}\n")
    f.write(f"NIM: {nim}\n")
    f.write(f"Resolusi: {kata_kata}\n")
    
    print(f"File {nama_file} berhasil dibuat!")