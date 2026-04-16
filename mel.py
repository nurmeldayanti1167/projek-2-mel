import random
peserta = []
while True:
    nama = input("Masukkan nama (ketik 'selesai' untuk stop): ")
    if nama.lower() == 'selesai': break
    peserta.append(nama)
    random.shuffle(peserta)
    tengah = len(peserta) // 2
tim_a = peserta[:tengah]
tim_b = peserta[tengah:]