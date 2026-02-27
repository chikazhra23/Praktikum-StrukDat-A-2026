from kurs import kurs

def idr_ke_mata_uang(jumlah_idr, kode):
    return jumlah_idr / kurs[kode]

def mata_uang_ke_idr(jumlah, kode):
    return jumlah * kurs[kode]