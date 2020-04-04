#Nomor 1
class MhsTif(object):
    def __init__(self,nama,nim,kota,uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya.'
        return s

c0 = MhsTif("rudi", 10, "sukoharjo", 280000)
c1 = MhsTif("budi", 51, "klaten", 290000)
c2 = MhsTif("judi", 2, "Surakarta", 270000)
c3 = MhsTif("bobi", 18, "Boyolali", 235000)
c4 = MhsTif("andi", 4, "Semarang", 240000)
c5 = MhsTif("Alip", 31, "Salatiga", 250000)
c6 = MhsTif("Dodit", 13, "Klaten", 245000)
c7 = MhsTif("yudha", 5, "sukoharjo", 245000)
c8 = MhsTif("rizki", 23, "jepara", 245000)
c9 = MhsTif("Loki", 64, "Karanganyar", 270000)
c10 = MhsTif("Diandra", 29, "Purwodadi", 265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def urutkanNIM(a):
    baru = {}
    for i in range(len(a)):
        baru[a[i].nama] = a[i].nim
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elem in listofTuples:
        print (elem[0], ':', elem[1])

urutkanNIM(Daftar)

