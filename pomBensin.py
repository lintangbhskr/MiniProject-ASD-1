class PomBensin:
    def __init__(self, jenis, harga, jumlah, metode_pembayaran):
        self.jenis = jenis
        self.harga = harga
        self.jumlah = jumlah
        self.metode_pembayaran = metode_pembayaran

    def total_pembayaran(self):
        return self.harga * self.jumlah

class ListPomBensin:
    def __init__(self):
        self.daftar_pom = []

    def tambah_data(self, pom):
        self.daftar_pom.append(pom)
        print("Data berhasil ditambahkan!")

    def lihat_data(self):
        if not self.daftar_pom:
            print("Belum ada data pom bensin.")
        else:
            for index, pom in enumerate(self.daftar_pom):
                print("=== Pom Bensin {} ===".format(index + 1))
                print("Jenis Bahan Bakar:", pom.jenis)
                print("Harga/liter:", pom.harga)
                print("Jumlah liter:", pom.jumlah)
                print("Metode Pembayaran:", pom.metode_pembayaran)
                print("Total Pembayaran:", pom.total_pembayaran())
                print()

    def edit_data(self, index, pom_baru):
        if index < 0 or index >= len(self.daftar_pom):
            print("Indeks tidak valid.")
        else:
            self.daftar_pom[index] = pom_baru
            print("Data berhasil diubah!")

    def hapus_data(self, index):
        if index < 0 or index >= len(self.daftar_pom):
            print("Indeks tidak valid.")
        else:
            del self.daftar_pom[index]
            print("Data berhasil dihapus!")

# Fungsi untuk membuat data pom bensin
def buat_pom_bensin(jenis, harga):
    jumlah = int(input(f"Masukkan jumlah liter {jenis}: "))
    print("Pilih Metode Pembayaran:")
    print("1. Cash")
    print("2. Debit")
    metode_pilihan = input("Masukkan pilihan (1/2): ")
    metode_pembayaran = "Cash" if metode_pilihan == "1" else "Debit"
    return PomBensin(jenis, harga, jumlah, metode_pembayaran)

# Main program
if __name__ == "__main__":
    list_pom = ListPomBensin()
    jenis_bbm = {
        "1": ("Pertalite", 10000),
        "2": ("Pertamax", 13500),
        "3": ("Pertamax Turbo", 14750)
    }

    while True:
        print("\n=== Aplikasi CRUD Pom Bensin ===")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            print("Pilih Jenis Bahan Bakar:")
            for key, value in jenis_bbm.items():
                print(f"{key}. {value[0]} - Harga/liter: {value[1]}")
            jenis_pilihan = input("Masukkan pilihan (1/2/3): ")
            if jenis_pilihan in jenis_bbm:
                jenis, harga = jenis_bbm[jenis_pilihan]
                pom_baru = buat_pom_bensin(jenis, harga)

                # Menampilkan preview data yang akan ditambahkan
                print("\nBerikut data yang anda input:")
                print("Jenis Bahan Bakar:", pom_baru.jenis)
                print("Harga/liter:", pom_baru.harga)
                print("Jumlah liter:", pom_baru.jumlah)
                print("Metode Pembayaran:", pom_baru.metode_pembayaran)
                print("Total Pembayaran:", pom_baru.total_pembayaran())

                konfirmasi = input("\nApakah data di atas sudah benar? (y/n): ")
                if konfirmasi.lower() == "y":
                    list_pom.tambah_data(pom_baru)
            else:
                print("Pilihan tidak valid.")
        elif pilihan == "2":
            list_pom.lihat_data()
        elif pilihan == "3":
            index = int(input("Masukkan indeks data yang ingin diubah: "))
            if index > 0 and index <= len(list_pom.daftar_pom):
                jenis, harga = list_pom.daftar_pom[index - 1].jenis, list_pom.daftar_pom[index - 1].harga
                pom_baru = buat_pom_bensin(jenis, harga)

                # Menampilkan preview data yang akan diubah
                print("\nBerikut data yang akan diubah:")
                print("Jenis Bahan Bakar:", pom_baru.jenis)
                print("Harga/liter:", pom_baru.harga)
                print("Jumlah liter:", pom_baru.jumlah)
                print("Metode Pembayaran:", pom_baru.metode_pembayaran)
                print("Total Pembayaran:", pom_baru.total_pembayaran())

                konfirmasi = input("\nApakah data di atas sudah benar? (y/n): ")
                if konfirmasi.lower() == "y":
                    list_pom.edit_data(index - 1, pom_baru)
            else:
                print("Indeks tidak valid.")
        elif pilihan == "4":
            index = int(input("Masukkan indeks data yang ingin dihapus: "))
            if index > 0 and index <= len(list_pom.daftar_pom):
                list_pom.hapus_data(index - 1)
            else:
                print("Indeks tidak valid.")
        elif pilihan == "5":
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
