class Orang:
    total_orang = 0
    def __init__(self, nama, nik, alamat):
        self.nama = nama
        self.__nik = nik
        self._alamat = alamat
        Orang.total_orang += 1
    @property
    def nik(self):
        return self.__nik
    @nik.setter
    def nik(self, val):
        if len(val) != 16:
            raise ValueError("NIK harus 16 digit!")
        self.__nik = val
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Alamat: {self._alamat}")

class Pasien(Orang):
    def __init__(self, nama, nik, alamat, no_rm, riwayat_penyakit):
        super().__init__(nama, nik, alamat)
        self.no_rm = no_rm
        self.riwayat_penyakit = riwayat_penyakit
    def tampilkan_info(self):
        print(f"[Pasien] Nama: {self.nama}, Alamat: {self._alamat}, No RM: {self.no_rm}, Riwayat: {self.riwayat_penyakit}")

class Dokter(Orang):
    def __init__(self, nama, nik, alamat, id_dokter, spesialisasi):
        super().__init__(nama, nik, alamat)
        self.id_dokter = id_dokter
        self.spesialisasi = spesialisasi
    def tampilkan_info(self):
        print(f"[Dokter] Dr. {self.nama}, Spesialis: {self.spesialisasi}, ID: {self.id_dokter}, Alamat: {self._alamat}")

class RekamMedis:
    def __init__(self, tanggal, diagnosa):
        self.tanggal = tanggal
        self.diagnosa = diagnosa

class Klinik:
    def __init__(self, nama_klinik):
        self.nama_klinik = nama_klinik
        self.daftar_dokter = []
    def tambah_dokter(self, dokter):
        self.daftar_dokter.append(dokter)
    def info_klinik(self):
        print(f"\n--- Informasi Klinik: {self.nama_klinik} ---")
        print("Daftar Dokter yang Bertugas:")
        for dokter in self.daftar_dokter:
            dokter.tampilkan_info()

if __name__ == "__main__":
    print("=== PENGUJIAN SISTEM KLINIK OOP ===")
    pasien1 = Pasien("Budi Santoso", "3201123456789012", "Jl. Merdeka No. 10", "RM001", "Demam Berdarah")
    dokter1 = Dokter("Andi", "3201987654321098", "Jl. Sehat No. 5", "DOC001", "Umum")
    print("\n--- Uji Method Overriding ---")
    pasien1.tampilkan_info()
    dokter1.tampilkan_info()
    klinik_sehat = Klinik("Klinik Sehat Bersama")
    klinik_sehat.tambah_dokter(dokter1)
    klinik_sehat.info_klinik()
    print("\n--- Uji Rekam Medis (Komposisi) ---")
    rm = RekamMedis("2026-10-07", "Infeksi saluran pernapasan ringan")
    print(f"Pasien {pasien1.nama} dengan No RM {pasien1.no_rm} mendapat diagnosa: {rm.diagnosa} pada tanggal {rm.tanggal}.")
