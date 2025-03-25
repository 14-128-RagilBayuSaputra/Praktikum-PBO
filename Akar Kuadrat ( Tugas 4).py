import math

def hitung_akar_kuadrat():
    while True:
        try:
            
            angka = input("Masukkan angka: ").strip()  
            
            if not angka:
                raise ValueError("Input tidak boleh kosong. Harap masukkan angka yang valid.")
            
            angka = float(angka)
            
            if angka < 0:
                raise ValueError("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                raise ValueError("Akar kuadrat dari nol tidak diperbolehkan.")
            
            hasil = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {hasil:.2f}")
            break  

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}. Harap masukkan angka yang valid.")

if __name__ == "__main__":
   hitung_akar_kuadrat()
