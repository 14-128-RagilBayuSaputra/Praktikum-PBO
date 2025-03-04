jumlah_siswa = int(input("masukkan jumlah siswa: "))
dictionary = {}

for i in range (jumlah_siswa):
    nama_siswa = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai_siswa = int(input(f"Masukkan nilai untuk {nama_siswa}: "))
    dictionary[nama_siswa] = nilai_siswa
    
print(dictionary) 
                            