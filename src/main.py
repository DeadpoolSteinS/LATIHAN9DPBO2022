from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *


# first data
hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, "Jakarta", 10000000))
hunians.append(Rumah("Gustavo Fring", 5, 2, "Bandung", 5000000))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", "Yogyakarta", 1000000))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, "Jakarta", 8000000))


# main frame
root = Tk()
root.title("Praktikum DPBO Python")



# function for show detail of residen
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    def closeTopLevel():
        top.destroy()

    b_exit = Button(opts, text="Exit", command=lambda : closeTopLevel())
    b_exit.grid(row=0, column=0)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")



# function for show dokumen of residen
def dokumen(index):
    top = Toplevel()
    top.title("Dokumen " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Dokumen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    def closeTopLevel():
        top.destroy()

    b_exit = Button(opts, text="Exit", command=lambda : closeTopLevel())
    b_exit.grid(row=0, column=0)

    d_summary = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=0, column=0, sticky="w")



# function for add indekos residen
def addIndekos():
    top = Toplevel()
    top.title("Tambah Data Residen")

    d_frame = LabelFrame(top, text="Form Data", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_owner = Label(d_frame, text="Nama Pemilik :", width=15, font=("bold",10), anchor="w").grid(row=0, column=0, sticky="w")
    input_type = Entry(d_frame, width=30).grid(row=0, column=1)

    d_occupant = Label(d_frame, text="Nama Penghuni :", width=15, font=("bold",10), anchor="w").grid(row=1, column=0, sticky="w")
    input_occupant = Entry(d_frame, width=30).grid(row=1, column=1)



# function for add not indekos residen
def addNotIndekos():
    top = Toplevel()
    top.title("Tambah Data Residen")

    d_frame = LabelFrame(top, text="Form Data", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_owner = Label(d_frame, text="Nama Pemilik :", width=15, font=("bold",10), anchor="w").grid(row=0, column=0, sticky="w")
    input_owner = Entry(d_frame, width=30).grid(row=0, column=1)

    d_total_occupant = Label(d_frame, text="Jumlah Penghuni :", width=15, font=("bold",10), anchor="w").grid(row=1, column=0, sticky="w")
    input_total_occupant = Entry(d_frame, width=30).grid(row=1, column=1)

    d_total_room = Label(d_frame, text="Jumlah Kamar :", width=15, font=("bold",10), anchor="w").grid(row=2, column=0, sticky="w")
    input_total_room = Entry(d_frame, width=30).grid(row=2, column=1)



# isi frame utama
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)



# button add and exit
b_indekos = Button(opts, text="Add Indekos", command=lambda : addIndekos(), state="disabled")
b_indekos.grid(row=0, column=0)

b_not_indekos = Button(opts, text="Add Not Indekos", command=lambda : addNotIndekos(), state="disabled")
b_not_indekos.grid(row=0, column=1)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=2)


# header table
idx = Label(frame, text="No", width=5, borderwidth=1, relief="solid")
idx.grid(row=0, column=0)

type = Label(frame, text="Jenis Residen", width=15, borderwidth=1, relief="solid")
type.grid(row=0, column=1)

name = Label(frame, text="Pemilik", width=20, borderwidth=1, relief="solid", anchor="w")
name.grid(row=0, column=2)

name = Label(frame, text="Penghuni", width=20, borderwidth=1, relief="solid", anchor="w")
name.grid(row=0, column=3)

name = Label(frame, text="Jumlah Kamar", width=15, borderwidth=1, relief="solid", anchor="w")
name.grid(row=0, column=4)

name = Label(frame, text="Action", width=15, borderwidth=1, relief="solid")
name.grid(row=0, column=5)


# isi table
for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index+1, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index+1, column=1)

    name = Label(frame, text=" " + h.get_nama_pemilik(), width=20, borderwidth=1, relief="solid", anchor="w")
    name.grid(row=index+1, column=2)

    if h.get_jenis() == "Indekos": 
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=20, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index+1, column=3)
    else:
        name = Label(frame, text="-", width=20, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index+1, column=3)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_jml_kamar(), width=15, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index+1, column=4)
    else:
        name = Label(frame, text="-", width=15, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index+1, column=4)

    action = LabelFrame(frame)
    action.grid(row=index+1, column=5)

    b_detail = Button(action, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=0, column=0)
    b_detail = Button(action, text="Dokumen ", command=lambda index=index: dokumen(index))
    b_detail.grid(row=0, column=1)

root.mainloop()
