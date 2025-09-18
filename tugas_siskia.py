# Input data nilai
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS  : "))
uas = float(input("Masukkan nilai UAS  : "))

# Bobot
bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40

# Hitung nilai akhir per komponen
nilai_akhir_tugas = tugas * bobot_tugas
nilai_akhir_uts = uts * bobot_uts
nilai_akhir_uas = uas * bobot_uas

# Hitung total nilai akhir
total_nilai_akhir = nilai_akhir_tugas + nilai_akhir_uts + nilai_akhir_uas

# Tampilkan hasil
print("\n--- Nilai yang Kamu Peroleh ---")
print(f"Nilai Tugas: {tugas}")
print(f"Nilai UTS  : {uts}")
print(f"Nilai UAS  : {uas}")
print("-------------------------------")
print(f"Nilai akhir dari Tugas (30%): {nilai_akhir_tugas}")
print(f"Nilai akhir dari UTS (30%): {nilai_akhir_uts}")
print(f"Nilai akhir dari UAS (40%): {nilai_akhir_uas}")
print("-------------------------------")
print(f"Total Nilai Akhir Kamu: {total_nilai_akhir}")
