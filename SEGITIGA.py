def print_segitiga(tinggi):
    print(f"tinggi: {tinggi}")
    for i in range(1, tinggi + 1):
        spaces = ' ' * (tinggi - i)
        bintang = '*' * (2 * i - 1)
        print(spaces + bintang)
        
tinggi = int(input("Masukkan Tinggi Segitiga : "))
print_segitiga(tinggi)