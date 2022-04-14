from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni = 1, jml_kamar = 1, lokasi = "", harga = 0):
        super().__init__("Apartemen", lokasi, harga, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik