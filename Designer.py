"""
Saya Aldi Saepurahman mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak
melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
"""
#import class Manusia
from Manusia import Manusia
#buat class Designer yang merupakan turunan class Manusia
class Designer(Manusia):
    #constructor dengan memanggil constructor kelas manusia dan inisialisasi posisi designer
    def __init__(self, noktp, nama, jk, gaji, position, foto):
        super().__init__(noktp, nama, jk, gaji, "Designer", foto)
        self.position = position
    #get posisi designer
    def getPosition(self):
        return self.position
        