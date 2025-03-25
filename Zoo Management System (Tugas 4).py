from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name, species):
        self.__name = name  
        self.__species = species  
    
    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"{self.__name} adalah seekor {self.__species}."

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name, "Anjing")
    
    def make_sound(self):
        return "Guk guk!"

class Cat(Animal):
    
    def __init__(self, name):
        super().__init__(name, "Kucing")
    
    def make_sound(self):
        return "Meong!"

class Bird(Animal):
    
    def __init__(self, name):
        super().__init__(name, "Burung")
    
    def make_sound(self):
        return "Cuit cuit!"

class ZooManagement:
    
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Hanya objek turunan dari Animal yang bisa ditambahkan.")
        
        self.animals.append(animal)
        print(f"{animal.get_info()} berhasil ditambahkan ke kebun binatang.")

    def show_animals(self):
        if not self.animals:
            print("Tidak ada hewan di kebun binatang.")
        else:
            print("\nDaftar Hewan di Kebun Binatang:")
            for animal in self.animals:
                print(f"- {animal.get_info()} dan bersuara '{animal.make_sound()}'")

def main():
    zoo = ZooManagement()

    while True:
        print("\n=== Sistem Manajemen Hewan ===")
        print("1. Tambah Hewan")
        print("2. Tampilkan Daftar Hewan")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ").strip()

        if pilihan == "1":
            print("\nJenis Hewan yang Bisa Ditambahkan:")
            print("1. Anjing")
            print("2. Kucing")
            print("3. Burung")

            jenis = input("Pilih jenis hewan (1/2/3): ").strip()
            nama = input("Masukkan nama hewan: ").strip()

            try:
                if not nama:
                    raise ValueError("Nama hewan tidak boleh kosong.")
                
                if jenis == "1":
                    hewan = Dog(nama)
                elif jenis == "2":
                    hewan = Cat(nama)
                elif jenis == "3":
                    hewan = Bird(nama)
                else:
                    raise ValueError("Pilihan jenis hewan tidak valid.")

                zoo.add_animal(hewan)
            
            except ValueError as e:
                print(f"Error: {e}")

        elif pilihan == "2":
            zoo.show_animals()
        
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        
        else:
            print("Input tidak valid. Pilih opsi 1, 2, atau 3.")

if __name__ == "__main__":
    main()
