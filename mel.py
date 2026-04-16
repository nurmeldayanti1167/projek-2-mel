import random
peserta = []
while True:
    nama = input("Masukkan nama (ketik 'selesai' untuk stop): ")
    if nama.lower() == 'selesai': break
    peserta.append(nama)
    random.shuffle(peserta)