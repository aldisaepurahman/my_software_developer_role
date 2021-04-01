"""
Saya Aldi Saepurahman mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak
melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
"""
"""import class Programmer, Designer, tkinter, font, PIL, messagebox, filedialog,
serta class operasi file"""
from Programmer import Programmer
from Designer import Designer
from tkinter import *
from tkinter import font
from PIL import ImageTk
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import shutil, os
#deklarasikan list kosong menampung data hasil submit
submissions = []
#setting path import gambar
path = "D:\KULIAH\PBO\Python\Praktikum3\software-dev-role\images"
#buat aplikasi dengan title Software Developer Role
root = Tk()
root.title("Software Developer Role")
#setting font aplikasi dengan calibri light bold berukuran 16px 
defaultfont = font.nametofont("TkDefaultFont")
defaultfont.configure(family="Calibri Light", size=16, weight=font.BOLD)
#buat list posisi pekerjaannya
listPosition = ['Frontend Programmer', 'Backend Programmer', 'Data Designer', 'UI/UX Designer',
'Architecture Designer', 'Module Designer']
#buat dictionary untuk mengecek posisi pekerjaan mana yang user pilih
selectorPosition = {item:IntVar() for item in listPosition}
#buat checker untuk mengecek pilihan dropdown user
checker = StringVar()
#prosedur menampilkan detail pegawai ketika menekan tombol details dari frame submissions
def details(index):
    #buat top level
    top = Toplevel()
    top.title("Detail" + submissions[index].getRole())

    #buat frame baru
    topframe = LabelFrame(top, text="Detail" + submissions[index].getRole(), padx=10, pady=10)
    topframe.pack(padx=10, pady=10)

    #buat frame khusus data
    detailframe = LabelFrame(topframe, padx=5, pady=5, borderwidth = 0, highlightthickness = 0)
    detailframe.grid(row=0, column=0)

    #buat frame khusus tombol close
    bottomframe = LabelFrame(top, padx=10, pady=10, borderwidth = 0, highlightthickness = 0)
    bottomframe.pack(padx=10, pady=10, anchor="e")

    #buat tombol close frame detail
    btnClose = Button(bottomframe, text="Close", width=10, command=top.destroy)
    btnClose.grid(row=0, column=0, sticky="e")

    #buat frame khusus menampilkan foto di dalam frame data
    frmfoto = LabelFrame(topframe, padx=5, pady=5, borderwidth = 0, highlightthickness = 0)
    frmfoto.grid(row=0, column=1)

    #tampilkan secara berurutan data ktp, nama, jenis kelamin, gaji, posisi, dan platform (khusus Programmer)
    lblktp = Label(detailframe, text="Nomor KTP", width=20, borderwidth=1, relief="solid", anchor="w")
    lblktp.grid(row=0, column=0)

    lblktpreq = Label(detailframe, text=submissions[index].getNoKtp(), width=50, borderwidth=1, relief="solid", anchor="w")
    lblktpreq.grid(row=0, column=1)

    lblnama = Label(detailframe, text="Nama", width=20, borderwidth=1, relief="solid", anchor="w")
    lblnama.grid(row=1, column=0)

    lblnamareq = Label(detailframe, text=submissions[index].getNama(), width=50, borderwidth=1, relief="solid", anchor="w")
    lblnamareq.grid(row=1, column=1)

    lbljk = Label(detailframe, text="Jenis Kelamin", width=20, borderwidth=1, relief="solid", anchor="w")
    lbljk.grid(row=2, column=0)

    lbljkreq = Label(detailframe, text=submissions[index].getJK(), width=50, borderwidth=1, relief="solid", anchor="w")
    lbljkreq.grid(row=2, column=1)

    lblsalary = Label(detailframe, text="Gaji", width=20, borderwidth=1, relief="solid", anchor="w")
    lblsalary.grid(row=3, column=0)

    lblsalaryreq = Label(detailframe, text=submissions[index].getGaji(), width=50, borderwidth=1, relief="solid", anchor="w")
    lblsalaryreq.grid(row=3, column=1)

    lblpos = Label(detailframe, text="Posisi", width=20, borderwidth=1, relief="solid", anchor="w")
    lblpos.grid(row=4, column=0)

    #jika data mengenai programmer dipilih semua, maka posisinya adalah fullstack programmer
    if submissions[index].getRole() == "Programmer" and len(submissions[index].getPosition()) == 2:
        viewPos = "Fullstack Programmer"
    #jika data mengenai designer dipilih semua, maka posisinya adalah complete designer
    elif submissions[index].getRole() == "Designer" and len(submissions[index].getPosition()) == 4:
        viewPos = "Complete Designer"
    #jika tidak, tampilkan sesuai data yang dipilih
    else:
        viewPos = ", ".join(submissions[index].getPosition())

    lblposreq = Label(detailframe, text=viewPos, width=50, borderwidth=1, relief="solid", anchor="w")
    lblposreq.grid(row=4, column=1)

    if submissions[index].getRole() == "Programmer":
        lblplatform = Label(detailframe, text="Fokus Pada Platform", width=20, borderwidth=1, relief="solid", anchor="w")
        lblplatform.grid(row=5, column=0)

        lblplatformreq = Label(detailframe, text=submissions[index].getPlatform(), width=50, borderwidth=1, relief="solid", anchor="w")
        lblplatformreq.grid(row=5, column=1)

    #tampilkan foto dari folder import, dengan ukuran 150x150
    file_path = os.path.join(path, submissions[index].getFoto())
    img = Image.open(file_path)
    reimage = img.resize((150, 150))
    images = ImageTk.PhotoImage(reimage)
    lblImg = Label(frmfoto, image=images)
    lblImg.image = images
    lblImg.pack()
#prosedur menampilkan semua data hasil submit ketika menekan tombol see all submissions
def viewAllSubmissions():
    #jika ada datanya, buat frame baru dan tampilkan data nama dan rolenya
    if len(submissions) > 0:
        top = Toplevel()
        top.title("Submissions")

        topframe = LabelFrame(top, text="Submissions", padx=10, pady=10)
        topframe.pack(padx=10, pady=10)

        bottomframe = LabelFrame(top, padx=10, pady=10, borderwidth = 0, highlightthickness = 0)
        bottomframe.pack(padx=10, pady=10, anchor="e")

        btnClose = Button(bottomframe, text="Close", width=10, command=top.destroy)
        btnClose.grid(row=0, column=0, sticky="e")

        for index, h in enumerate(submissions):
            idx = Label(topframe, text=str(index+1), width=5, borderwidth=1, relief="solid")
            idx.grid(row=index, column=0)

            nama = Label(topframe, text=h.getNama(), width=15, borderwidth=1, relief="solid")
            nama.grid(row=index, column=1)

            role = Label(topframe, text=" " + h.getRole(), width=40, borderwidth=1, relief="solid", anchor="w")
            role.grid(row=index, column=2)

            b_detail = Button(topframe, text="Details ", command=lambda index=index: details(index))
            b_detail.grid(row=index, column=3)
    #jika tidak ada, tampilkan pesan informasi
    else:
        msg = messagebox.showinfo("Informasi", "Tidak Ada Data Yang Masuk")
#prosedur ketika menekan tombol about
def aboutMe():
    #buat frame baru dan tampilkan deskripsi program serta data diri
    top = Toplevel()
    top.title("About")

    aboutframe = LabelFrame(top, text="SOFTWARE DEVELOPER ROLE", padx=10, pady=10)
    aboutframe.pack(padx=10, pady=10)

    bottomframe = LabelFrame(top, padx=10, pady=10, borderwidth = 0, highlightthickness = 0)
    bottomframe.pack(padx=10, pady=10, anchor="e")

    btnClose = Button(bottomframe, text="Close", width=10, command=top.destroy)
    btnClose.grid(row=0, column=0, sticky="e")

    teks = "Deskripsi : Aplikasi ini bernama SOFTWARE DEVELOPER ROLE. Dimana\nsoftware ini digunakan oleh perusahaan software house untuk mendata\nbidang keahlian karyawannya."
    deskripsi = Label(aboutframe, text=teks, justify="left", pady="5").grid(row=0, column=0, sticky="w")
    nim = Label(aboutframe, text="NIM: 1901942" , anchor="w", pady="5").grid(row=1, column=0, sticky="w")
    nama = Label(aboutframe, text="Nama : Aldi Saepurahman", anchor="w", pady="5").grid(row=2, column=0, sticky="w")

#prosedur ketika memilih role dari dropdown
def onSelectRole(*args):
    #jika memilih programmer
    if checker.get() == "Programmer":
        #set enabled radio button platform
        platformAndroid = Radiobutton(platformframe, text="Android", variable=idxPlatform, value=1, command=setPlatform).grid(row=0, column=0, sticky="w")
        platformDesktop = Radiobutton(platformframe, text="Desktop", variable=idxPlatform, value=2, command=setPlatform).grid(row=0, column=1, sticky="w")
        platformWeb = Radiobutton(platformframe, text="Web", variable=idxPlatform, value=3, command=setPlatform).grid(row=0, column=2, sticky="w")
    #jika memilih designer
    else:
        #set disabled radio button platform
        platformAndroid = Radiobutton(platformframe, text="Android", variable=idxPlatform, value=1, state="disabled", command=setPlatform).grid(row=0, column=0, sticky="w")
        platformDesktop = Radiobutton(platformframe, text="Desktop", variable=idxPlatform, value=2, state="disabled", command=setPlatform).grid(row=0, column=1, sticky="w")
        platformWeb = Radiobutton(platformframe, text="Web", variable=idxPlatform, value=3, state="disabled", command=setPlatform).grid(row=0, column=2, sticky="w")
        
    #cek pada check button, bila ada posisi yang terkait dengan rolenya, checkbutton di set normal, jika tidak tetap disabled
    for item in range(len(listPosition)):
        cbPosition[item].deselect()
        if listPosition[item].find(checker.get()) != -1:
            cbPosition[item]['state'] = "normal"
        else:
            cbPosition[item]['state'] = "disabled"
#prosedur ketika memilih jenis kelamin
def setJk():
    #data pada textbox jenis kelamin (hidden) dihapus
    txtJk.delete(0, "end")
    #jika memilih 1, masukkan nilai laki-laki pada textbox
    if idx.get() == 1:
        txtJk.insert(0, "Laki-Laki")
    #jika memilih 2, masukkan nilai perempuan pada textbox
    else:
        txtJk.insert(0, "Perempuan")
#prosedur ketika memilih platform
def setPlatform():
    #data pada textbox platform (hidden) dihapus
    txtPlatform.delete(0, "end")
    #jika memilih 1, masukkan nilai android pada textbox
    if idxPlatform.get() == 1:
        txtPlatform.insert(0, "Android")
    #jika memilih 2, masukkan nilai desktop pada textbox
    elif idxPlatform.get() == 2:
        txtPlatform.insert(0, "Desktop")
    #jika memilih 3, masukkan nilai web pada textbox
    elif idxPlatform.get() == 3:
        txtPlatform.insert(0, "Web")
#prosedur ketika tombol choose foto ditekan
def openFoto():
    #set textbox foto dalam keadaan normal dan hapus data pada textbox foto dan path (hidden)
    txtFoto.configure(state='normal')
    txtFoto.delete(0, "end")
    txtPath.delete(0, "end")
    #buka file dialog
    filename = filedialog.askopenfilename()
    #ambil nama fotonya
    foto = os.path.basename(filename)
    #masukkan path dan nama fotonya kedalam textbox
    txtPath.insert(0, filename)
    txtFoto.insert(0, foto)
    #set textbox foto kedalam keadaan readonly
    txtFoto.configure(state='readonly')
#prosedur ketika data hasil submit sukses
def clear():
    #hapus semua data pada kolom inputan
    txtKtp.delete(0, "end")
    txtNama.delete(0, "end")
    txtJk.delete(0, "end")
    txtGaji.delete(0, "end")
    txtFoto.configure(state='normal')
    txtFoto.delete(0, "end")
    idxPlatform.set(0)
    idx.set(0)
    txtPlatform.delete(0, "end")
    rolechoosen.set('')

    for item in range(len(listPosition)):
        cbPosition[item].deselect()
        cbPosition[item]['state'] = "disabled"
#prosedur ketika tombol submit ditekan
def onSubmit():
    #jika textbox ktp, nama, jenis kelamin, gaji, foto, dan dropdown bernilai
    if txtKtp.get() != "" and txtNama.get() != "" and txtJk.get() != "" and txtGaji.get() != "" and txtFoto.get() != "" and (checker.get() == "Programmer" or checker.get() == "Designer"):
        #cek apakah pada checkbox ada yang terpilih
        flag = False
        for key, value in selectorPosition.items():
            if value.get() == 1:
                flag = True
        #jika tidak ada yang terpilih, tampilkan pesan error
        if flag == False:
            msg = messagebox.showerror("Error", "Data Yang dimasukkan harus lengkap")
        #jika ada
        else:
            #jika role yang dipilih programmer dan platform tidak memilih, tampilkan pesan error
            if checker.get() == "Programmer" and txtPlatform.get() == "":
                msg = messagebox.showerror("Error", "Data Yang dimasukkan harus lengkap")
            #jika memilih
            else:
                #ambil semua data inputan
                noktp = txtKtp.get()
                nama = txtNama.get()
                jk = txtJk.get()
                gaji = txtGaji.get()
                photo = txtFoto.get()

                #join pathnya dengan nama foto inputan dan pindahkan ke path tujuan
                file_path = os.path.join(path, photo)
                shutil.copy(txtPath.get(), file_path)
                #buat list kosong menampung posisi pegawai
                positions = []

                #cari dalam dictionary, jika ada yang dipilih, masukkan pada list posisi
                for key, value in selectorPosition.items():
                    if value.get() == 1:
                        positions.append(key)
                #jika memilih programmer, ambil data platformnya dan masukkan bersama data lainnya kedalam list submissions
                if checker.get() == "Programmer":
                    platform = txtPlatform.get()
                    submissions.append(Programmer(noktp, nama, jk, gaji, positions, platform, photo))
                #jika memilih designer, masukkan semua data inputan kedalam list submissions
                else:
                    submissions.append(Designer(noktp, nama, jk, gaji, positions, photo))
                
                #tampilkan pesan sukses
                msg = messagebox.showinfo("Informasi", "Data berhasil disimpan!")
                #hapus data pada form inputan
                clear()
    #jika tidak memenuhi validasi, tampilkan pesan error
    else:
        msg = messagebox.showerror("Error", "Data Yang dimasukkan harus lengkap")
#prosedur ketika tombol pesan dialog exit/clear submission ditekan yes
def clearAll():
    #hapus semua foto pada folder dari path dan hapus semua data dari list submissions
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    submissions.clear()
#prosedur ketika tombol clear submissions ditekan
def clearSubmissions():
    #munculkan pesan dialog
    msg = messagebox.askquestion("Warning", "Data yang sudah disimpan akan terhapus. Anda Yakin akan menghapusnya?")
    #jika menekan yes, hapus semua datanya
    if msg == 'yes':
        clearAll()
#prosedur ketika tombol exit ditekan
def onExit():
    #munculkan pesan dialog
    msg = messagebox.askquestion("Warning", "Data yang sudah disimpan akan terhapus. Anda Yakin akan keluar?")
    #jika menekan yes, hapus semua datanya dan keluar dari aplikasi
    if msg == 'yes':
        clearAll()
        root.destroy()
#buat frame utama aplikasi
mainframe = LabelFrame(root, padx=10, pady=10, borderwidth = 0, highlightthickness = 0)
mainframe.pack(padx=10, pady=10)
#buat frame khusus form
frmframe = LabelFrame(mainframe, padx=5, pady=5, borderwidth = 0, highlightthickness = 0)
frmframe.grid(row=0, column=0)
#buat frame khusus tombol submit
btnframe = LabelFrame(mainframe, padx=5, pady=5, borderwidth = 0, highlightthickness = 0)
btnframe.grid(row=1, column=0, sticky="e")
#buat frame khusus menu tombol about, see submission dan clear
menuframe = LabelFrame(mainframe, pady=5, borderwidth = 0, highlightthickness = 0)
menuframe.grid(row=0, column=1, padx=(50, 5))
#buat frame khusus tombol exit
exitframe = LabelFrame(mainframe, pady=5, borderwidth = 0, highlightthickness = 0)
exitframe.grid(row=1, column=1, padx=(50, 5))
#buat secara terurut kolom inputan nomor ktp, nama, jenis kelamin, gaji, role, posisi, platform dan foto
lblKtp = Label(frmframe, text="Nomor KTP", anchor="w", pady=5).grid(row=0, column=0, sticky="w")
txtKtp = Entry(frmframe, relief="solid", width=45)
txtKtp.grid(row=0, column=1, sticky="w")

lblNama = Label(frmframe, text="Nama", anchor="w", pady=5).grid(row=1, column=0, sticky="w")
txtNama = Entry(frmframe, relief="solid", width=45)
txtNama.grid(row=1, column=1, sticky="w")

lblGaji = Label(frmframe, text="Gaji", anchor="w", pady=5).grid(row=3, column=0, sticky="w")
txtGaji = Entry(frmframe, relief="solid", width=45)
txtGaji.grid(row=3, column=1, sticky="w")

lblJK = Label(frmframe, text="Jenis Kelamin", anchor="w", pady=5).grid(row=2, column=0, sticky="w")
#buat frame khusus jenis kelamin untuk dibuat inline
jkframe = LabelFrame(frmframe, pady=5, borderwidth = 0, highlightthickness = 0)
jkframe.grid(row=2, column=1, sticky="w")
#buat indeks radio button ketika dipilih
idx = IntVar()
#buat textbox untuk menampung nilai radio button jenis kelamin
txtJk = Entry(frmframe, relief="solid", width=45)
jkLaki = Radiobutton(jkframe, text="Laki-Laki", variable=idx, value=1, command=setJk)
jkLaki.grid(row=0, column=0, sticky="w")
jkPerempuan = Radiobutton(jkframe, text="Perempuan", variable=idx, value=2, command=setJk)
jkPerempuan.grid(row=0, column=1, sticky="w")

lblRole = Label(frmframe, text="Role", anchor="w", pady=5).grid(row=4, column=0, sticky="w")
rolechoosen = ttk.Combobox(frmframe, width = 43, textvariable = checker)
#buat dropdown dengan readonly agar data didalamnya tidak dimanipulasi user
rolechoosen['state'] = "readonly"
rolechoosen['values'] = ('Programmer', 'Designer')
rolechoosen.current()
rolechoosen.grid(row=4, column=1, sticky="w")
#panggil prosedur selectrole ketika dropdown dipilih
checker.trace_variable("w", onSelectRole)

lblPosition = Label(frmframe, text="Position", anchor="w", pady=5).grid(row=5, column=0, sticky="w")
#buat frame khusus checkbutton posisi
cbframe = LabelFrame(frmframe, pady=5, borderwidth = 0, highlightthickness = 0)
cbframe.grid(row=5, column=1, sticky="w")
#buat list untuk mendesain checkbutton sebanyak isi list posisi
baris = 0
kolom = 0
cbPosition = [None for item in range(len(listPosition))]
#desain checkboxnya
for item in range(len(listPosition)):
    cbPosition[item] = Checkbutton(cbframe, text=listPosition[item], variable=selectorPosition[listPosition[item]], onvalue=1, offvalue=0)
    cbPosition[item].grid(row=baris, column=kolom, sticky="w")
    if kolom == 1:
        kolom = 0
        baris += 1
    else:
        kolom += 1
    
    cbPosition[item]['state'] = "disabled"

lblPlatform = Label(frmframe, text="Fokus Pada Plaform", anchor="w", pady=5).grid(row=6, column=0, sticky="w")
#buat frame khusus platform untuk dibuat inline
platformframe = LabelFrame(frmframe, pady=5, borderwidth = 0, highlightthickness = 0)
platformframe.grid(row=6, column=1, sticky="w")
#buat indeks radio button platform ketika dipilih
idxPlatform = IntVar()
#buat textbox untuk menampung nilai radio button platform
txtPlatform = Entry(frmframe, relief="solid", width=30)
platformAndroid = Radiobutton(platformframe, text="Android", variable=idxPlatform, value=1, state="disabled", command=setPlatform)
platformAndroid.grid(row=0, column=0, sticky="w")
platformDesktop = Radiobutton(platformframe, text="Desktop", variable=idxPlatform, value=2, state="disabled", command=setPlatform)
platformDesktop.grid(row=0, column=1, sticky="w")
platformWeb = Radiobutton(platformframe, text="Web", variable=idxPlatform, value=3, state="disabled", command=setPlatform)
platformWeb.grid(row=0, column=2, sticky="w")

lblFoto = Label(frmframe, text="Foto", anchor="w", pady=5).grid(row=7, column=0, sticky="w")
#buat frame khusus foto untuk dibuat inline
fotoframe = LabelFrame(frmframe, pady=5, borderwidth = 0, highlightthickness = 0)
fotoframe.grid(row=7, column=1, sticky="w")
#buat textbox untuk menampung nilai radio button path dan nama fotonya
txtPath = Entry(fotoframe, relief="solid", width=40)
txtFoto = Entry(fotoframe, relief="solid", width=37)
txtFoto.grid(row=0, column=0, sticky="w")
btnChoose = Button(fotoframe, text="Choose..", command=openFoto)
btnChoose.grid(row=0, column=1, sticky="w", padx=(10, 0))
#buat tombol submit
btnSubmit = Button(btnframe, text="Submit", width=10, command=onSubmit).grid(row=0, column=0, sticky="e")
#khusus judul aplikasi diset ukuran 30px
lblNameApp = Label(menuframe, text="SOFTWARE\nDEVELOPER\nROLE", justify="left", pady=5)
lblNameApp.config(font = ("Calibri Light", 30, "bold"))
lblNameApp.grid(row=0, column=0, sticky="w")
#buat label deskripsi
lblDeskripsi = Label(menuframe, text="Program ini digunakan untuk\nmemilah peran pengembang\nsoftware di perusahaan", justify="left").grid(row=1, column=0, sticky="w", pady=(5, 25))
#buat tombol see submissions, clear submissions, about dan exit
btnListSubmission = Button(menuframe, text="See All Submissions", width=23, command=viewAllSubmissions).grid(row=2, column=0, sticky="w", pady=5)
btnClearSubmission = Button(menuframe, text="Clear Submissions", width=23, command=clearSubmissions).grid(row=3, column=0, sticky="w", pady=5)
btnAbout = Button(menuframe, text="About", width=23,command=aboutMe).grid(row=4, column=0, sticky="w", pady=(5, 30))
btnExit = Button(exitframe, text="Exit", width=23, command=onExit).grid(row=8, column=0, sticky="w")
#generate main loop
root.mainloop()