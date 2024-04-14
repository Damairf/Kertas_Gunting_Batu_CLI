import time
import random

kertas = 1
gunting = 2
batu = 3
raya = random.randint(1, 3)

print('Permainan Kertas, Gunting, Batu melawan Raya')
print('(1) Kertas\n(2) Gunting\n(3) Batu')
while True:
    player = int(input('Silahkan masukkan antara nomor 1 sampai 3: '))
    if player < 1 or player > 3:
        print('Nomor tidak valid. Silahkan masukkan nomor antara 1 sampai 3')
    else:
        break

print()
if player == 1:
    print('Kamu memilih Kertas')
    print('Menunggu Raya memilih jawaban...')
    time.sleep(2)
    print()
    print('Hasil:')
    time.sleep(1)
    if raya == 1:
        print('Raya memilih Kertas')
        time.sleep(0.5)
        print('Kertas vs Kertas')
        time.sleep(0.5)
        print('Hasil Seri')
    elif raya == 2:
        print('Raya memilih Gunting')
        time.sleep(0.5)
        print('Kertas vs Gunting')
        time.sleep(0.5)
        print('Kamu Kalah')
    elif raya == 3:
        print('Raya memilih Batu')
        time.sleep(0.5)
        print('Kertas vs Batu')
        time.sleep(0.5)
        print('Kamu Menang')

if player == 2:
    print('Kamu memilih Gunting')
    print('Menunggu Raya memilih jawaban...')
    time.sleep(2)
    print()
    print('Hasil:')
    time.sleep(1)
    if raya == 1:
        print('Raya memilih Kertas')
        time.sleep(0.5)
        print('Gunting vs Kertas')
        time.sleep(0.5)
        print('Kamu Menang')
    elif raya == 2:
        print('Raya memilih Gunting')
        time.sleep(0.5)
        print('Gunting vs Gunting')
        time.sleep(0.5)
        print('Hasil Seri')
    elif raya == 3:
        print('Raya memilih Batu')
        time.sleep(0.5)
        print('Gunting vs Batu')
        time.sleep(0.5)
        print('Kamu Kalah')

if player == 3:
    print('Kamu memilih Batu')
    print('Menunggu Raya memilih jawaban...')
    time.sleep(2)
    print()
    print('Hasil:')
    time.sleep(1)
    if raya == 1:
        print('Raya memilih Kertas')
        time.sleep(0.5)
        print('Batu vs Kertas')
        time.sleep(0.5)
        print('Kamu Kalah')
    elif raya == 2:
        print('Raya memilih Gunting')
        time.sleep(0.5)
        print('Batu vs Gunting')
        time.sleep(0.5)
        print('Kamu Menang')
    elif raya == 3:
        print('Raya memilih Batu')
        time.sleep(0.5)
        print('Batu vs Batu')
        time.sleep(0.5)
        print('Hasil Seri')