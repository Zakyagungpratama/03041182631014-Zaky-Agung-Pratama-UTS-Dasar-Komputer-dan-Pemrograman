
# NAMA          : ZAKY AGUNG PRATAMA
# NIM           : 03041182631014
# KELAS         : INDRALAYA B
# MATA KULIAH   : DASAR KOMPUTER DAN PEMROGRAMAN (UTS)
# KASUS         : KELOMPOK F - Informasi/Data
# DOSEN PENGAMPU: ERIC SEAN KESUMA,S.T.,M.T

data_nilai = [  42, 55, 61, 68, 73,
                77, 82, 87, 91, 64,
                58, 76, 84, 49, 95,
                59, 60, 79, 80, 100 ]

#TESTING ADA 8 DATA

#data_nilai = [  57, 60, 62, 78,
#                80, 81, 30, 98 ]

# menentukan kategori (clear)
# menghitung rata-rata (clear)
# menghitung jumlah kategori (clear)

def kategori(nilai):
    if nilai < 60:
        return "RENDAH"
    elif nilai < 80:
        return "SEDANG"
    else:
        return "TINGGI"

def rata_rata(data):
    return sum(data) / len(data)

def hitung_kategori(data):
    rendah = 0
    sedang = 0
    tinggi = 0

    for nilai in data:
        if kategori(nilai) == "RENDAH":
            rendah += 1
        elif kategori(nilai) == "SEDANG":
            sedang += 1
        else:
            tinggi += 1
    return rendah, sedang, tinggi


print("===== ANALISIS DAN KLASIFIKASI DATA =====")

for i, nilai in enumerate(data_nilai, start=1):
    print(f"{i:02d}. Nilai = {nilai} -> {kategori(nilai)}")

rendah, sedang, tinggi = hitung_kategori(data_nilai)

print("\n===== RINGKASAN =====")
print("Total data :", len(data_nilai))
print("RENDAH     :", rendah)
print("SEDANG     :", sedang)
print("TINGGI     :", tinggi)
print("Rata-rata  :", round(rata_rata(data_nilai), 2))
print("Maksimum   :", max(data_nilai))
print("Minimum    :", min(data_nilai))
