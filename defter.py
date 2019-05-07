class AdresDefteri():
    'Adres Defteri Sınıfımız'
    kisiler = []
def __init__(self, isim):
        self.isim = isim
        self.numaralar = []
        self.kisiEkle()
        self.numaraEkle()
def kisiEkle(self):
        self.kisiler.append(self.isim)
        self.kisiler.append(self.numaralar)
        print("{},{} rehbere eklendi" .format(self.isim, self.numaralar))
def kisiyiGoruntule(self):
        print("Kisi Listesi:")
        for rehber in self.kisiler:
            print(rehber)
def numaraEkle(self, numaralar):
        self.numaralar.append(numaralar)
def numaralariGoruntule(self):
        print("{} isimli kisinin numaralari:".format(self.isim))
        for numaralar in self.numaralar:
            print(numaralar)




