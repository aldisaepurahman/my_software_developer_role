"""
Saya Aldi Saepurahman mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak
melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
"""
#buat class Manusia
class Manusia():
    """constructor terdiri dari nomor ktp, nama, jenis kelamin
    gaji, foto dan role di perusahaan"""
    def __init__(self, noktp, nama, jk, gaji, role, foto = ""):
        self.noktp = noktp
        self.nama = nama
        self.jk = jk
        self.gaji = gaji
        self.foto = foto
        self.role = role

    #get semua nilai atributnya
    def getNoKtp(self):
        return self.noktp

    def getNama(self):
        return self.nama

    def getJK(self):
        return self.jk

    def getGaji(self):
        return self.gaji

    def getFoto(self):
        return self.foto

    def getRole(self):
        return self.role
    