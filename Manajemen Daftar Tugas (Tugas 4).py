def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah_tugas(todo_list):
    try:
        tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
        if not tugas:
            raise ValueError("Tugas tidak boleh kosong.")
        
        todo_list.append(tugas)
        print("Tugas berhasil ditambahkan!")
    
    except ValueError as e:
        print(f"Error: {e}")

def hapus_tugas(todo_list):
    try:
        if not todo_list:
            raise ValueError("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
        
        nomor = input("Masukkan nomor tugas yang ingin dihapus: ").strip()
        if not nomor.isdigit():
            raise ValueError("Masukkan angka yang valid.")
        
        nomor = int(nomor)
        if nomor < 1 or nomor > len(todo_list):
            raise IndexError("Tugas dengan nomor tersebut tidak ditemukan.")
        
        tugas_dihapus = todo_list.pop(nomor - 1)
        print(f"Tugas '{tugas_dihapus}' berhasil dihapus.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")

def tampilkan_tugas(todo_list):
    if not todo_list:
        print("Daftar tugas kosong.")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(todo_list, 1):
            print(f"- {i}. {tugas}")

def main():
    todo_list = []
    
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

        if pilihan == "1":
            tambah_tugas(todo_list)
        elif pilihan == "2":
            hapus_tugas(todo_list)
        elif pilihan == "3":
            tampilkan_tugas(todo_list)
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Input tidak valid. Harap masukkan angka 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
