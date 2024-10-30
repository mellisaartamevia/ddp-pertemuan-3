# Definisikan fungsi untuk menghitung berat badan ideal
def hitung_berat_badan_ideal(tinggi):
    berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.1)
    return berat_ideal

# Contoh penggunaan program
tinggi = 165  # Contoh tinggi badan 165 cm
berat_ideal = hitung_berat_badan_ideal(tinggi)
print("Berat badan ideal untuk tinggi", tinggi, "cm adalah", round(berat_ideal, 2), "kg")

# Contoh lainnya
tinggi = 170  # Contoh tinggi badan 170 cm
berat_ideal = hitung_berat_badan_ideal(tinggi)
print("Berat badan ideal untuk tinggi", tinggi, "cm adalah", round(berat_ideal, 2), "kg")

# Contoh lainnya
tinggi = 175  # Contoh tinggi badan 175 cm
berat_ideal = hitung_berat_badan_ideal(tinggi)
print("Berat badan ideal untuk tinggi", tinggi, "cm adalah", round(berat_ideal, 2), "kg")

