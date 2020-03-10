from mahasiswa import Mahasiswa

mhs9 = Mahasiswa('Alhif', 3234234, 'Jabar', 20000)
mhs9.ambilKuliah('Ilmu Keislaman')
mhs9.ambilKuliah('Tafsir')
mhs9.ambilKuliah('Bahasa Arab')
print(mhs9.listKuliah)
mhs9.hapusKuliah('Tafsir')
print(mhs9.listKuliah)
