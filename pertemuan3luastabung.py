import math

def luas_permukaan_tabung(r, t):
    # Rumus luas permukaan tabung
    luas_permukaan = 2 * math.pi * r * (r + t)
    return luas_permukaan

def keliling_alas_tabung(r):
    # Rumus keliling alas tabung
    keliling_alas = 2 * math.pi * r
    return keliling_alas

# Contoh penggunaan
jari_jari = float(input("Masukkan jari-jari tabung (r): "))
tinggi = float(input("Masukkan tinggi tabung (t): "))

luas = luas_permukaan_tabung(jari_jari, tinggi)
keliling = keliling_alas_tabung(jari_jari)

print(f"Luas permukaan tabung: {luas:.2f}")
print(f"Keliling alas tabung: {keliling:.2f}")
