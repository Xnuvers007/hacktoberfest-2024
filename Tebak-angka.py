import random

def tebak_angka():
    print("Selamat datang di game Tebak Angka!")
    
    # Level of difficulty
    difficulty = input("Pilih tingkat kesulitan (easy, medium, hard): ").lower()
    
    if difficulty == "easy":
        max_number = 50
        max_attempts = 10
    elif difficulty == "medium":
        max_number = 100
        max_attempts = 7
    elif difficulty == "hard":
        max_number = 200
        max_attempts = 5
    else:
        print("Kesulitan tidak valid, menggunakan default (medium).")
        max_number = 100
        max_attempts = 7

    angka_rahasia = random.randint(1, max_number)
    tebakan = None
    jumlah_tebakan = 0

    print(f"Saya telah memilih angka antara 1 dan {max_number}. Anda punya {max_attempts} kali kesempatan untuk menebaknya!")

    while tebakan != angka_rahasia and jumlah_tebakan < max_attempts:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1

            # Check proximity for hints
            difference = abs(tebakan - angka_rahasia)
            if difference == 0:
                print(f"Selamat! Anda telah menebak angka {angka_rahasia} dengan {jumlah_tebakan} tebakan.")
                break
            elif difference <= 5:
                print("Sangat dekat!")
            elif difference <= 15:
                print("Cukup dekat!")
            else:
                print("Jauh sekali!")

            if tebakan < angka_rahasia:
                print("Terlalu rendah!")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi!")

        except ValueError:
            print("Silakan masukkan angka yang valid.")
        
        if jumlah_tebakan == max_attempts:
            print(f"Maaf, Anda kehabisan kesempatan. Angka rahasia adalah {angka_rahasia}.")

    # Option to play again
    play_again = input("Ingin bermain lagi? (ya/tidak): ").lower()
    if play_again == "ya":
        tebak_angka()
    else:
        print("Terima kasih telah bermain!")

# Menjalankan game
tebak_angka()