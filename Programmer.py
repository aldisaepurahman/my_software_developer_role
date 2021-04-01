"""
Saya Aldi Saepurahman mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak
melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
"""
#import class Manusia
from Manusia import Manusia
#buat class Programmer yang merupakan turunan class Manusia
class Programmer(Manusia):
    #constructor dengan memanggil constructor kelas manusia dan inisialisasi posisi dan fokus platform Programmer
    def __init__(self, noktp, nama, jk, gaji, position, platform, foto):
        super().__init__(noktp, nama, jk, gaji, "Programmer", foto)
        self.position = position
        self.platform = platform

    #get setiap atribut dari class Programmer
    def getPosition(self):
        return self.position

    def getPlatform(self):
        return self.platform

        