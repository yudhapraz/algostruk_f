class Manusia:
    keadaan = 'Kenyang'
    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print('Salam, namaku {}'.format(self.nama))

    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'Kenyang'

    def olahraga(self, k):
        print('Saya baru saja Olahraga', k)
        self.keadaan = 'Laparrr'

    def mengalikanDenganDua(self, n):
        return n * 2
