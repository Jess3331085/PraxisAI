# 1. prime
prime = [2,3,5,7]

nilaimax = max(prime)
print(nilaimax)

nilaimin = min(prime)
print(nilaimin) 


# 2. hitung huruf (teks):
a = 'budimukidi'

# Membuat dictionary untuk menyimpan frekuensi karakter
frequency = {}

# Menghitung frekuensi setiap karakter
for i in a:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

# Mencetak frekuensi karakter dalam format yang diinginkan
for char, count in frequency.items():
    print(f"{char}:{count}", end=', ') 


# 3. key & value dictionary
dict = {"murid":"jacindha", "sekolah":"praxis"}
print(dict)

# add
dict["alamat"] = input ("masukkan alamat")
print(dict)