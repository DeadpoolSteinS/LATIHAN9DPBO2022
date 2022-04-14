class Hunian():
    def __init__(self, jenis, lokasi = "", harga = 0, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.lokasi = lokasi
        self.harga = harga

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return str(self.jml_kamar)

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang. " + self.more()
    
    def more(self):
        return "Lokasi : " + self.lokasi + ", Harga : " + str(self.harga)