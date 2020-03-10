from mahasiswa import Mahasiswa

mhs = Mahasiswa('Rudi', 1212213, 'Sukoharjo', 270000)
# a
print(mhs.ambilKotaTinggal())

#b
mhs.perbaruiKotaTinggal('Bogor')
print(mhs.ambilKotaTinggal())

#c
print(mhs.ambilUangSaku())
mhs.tambahUangSaku(750000)
print(mhs.ambilUangSaku())
