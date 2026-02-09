import time
import random

def dramatic_print(text: str):
    print(text)
    time.sleep(0.5)


def print_win_ascii():
    ascii_win = """
    ╔═══════════════════════════════════╗
    ║   🎉  SELAMAT, KAMU MENANG! 🎉   ║
    ╚═══════════════════════════════════╝
    
      \\O/
       |
      / \\
    
    Kamu berhasil menyelamatkan diri dan 
    tiba dengan aman di rumah Nenek!
    """
    print(ascii_win)


def print_lose_ascii():
    ascii_lose = """
    ╔═══════════════════════════════════╗
    ║   💀  GAME OVER - NYAWA HABIS 💀  ║
    ╚═══════════════════════════════════╝
    
       |||
       |"|
      /| |\\
       | |
      /   \\
    
    Serigala telah menangkapmu...
    Cerita berakhir tragis.
    """
    print(ascii_lose)


def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")
    dramatic_print(f"Halo, {nama}. Kamu adalah Gadis Berkerudung Merah yang sedang menuju rumah nenek.")

    nyawa = 100
    menang = False

    dramatic_print(f"Kamu punya {nyawa} nyawa. Pilih jalurmu dengan bijak!")

    while nyawa > 0:
        dramatic_print("\nPilihan jalur:")
        dramatic_print("1) Rumah Nenek")
        dramatic_print("2) Hutan Serigala")
        pilihan = input("Ketik 'Rumah Nenek' atau 'Hutan Serigala': ").strip().lower()

        # Gunakan if-else untuk menangani pilihan
        if "rumah" in pilihan or "nenek" in pilihan:
            dramatic_print("Kamu memilih jalan aman menuju Rumah Nenek.")
            dramatic_print("Di depan rumah nenek, pintu sedikit terbuka dan lampu menyala redup.")
            dramatic_print("Ada dua opsi: ketuk pintu atau intip melalui jendela.")
            pilihan_rumah = input("Ketik 'Ketuk' atau 'Intip': ").strip().lower()
            
            if "ketuk" in pilihan_rumah or "pintu" in pilihan_rumah:
                # Elemen keberuntungan: ada 80% chance selamat
                keberuntungan = random.randint(1, 100)
                if keberuntungan <= 80:
                    dramatic_print("Nenek membuka pintu dengan senyum hangat.")
                    dramatic_print("Dia sangat senang melihat kamu membawa kue.")
                    print_win_ascii()
                    menang = True
                    break
                else:
                    dramatic_print("Saat pintu terbuka, serigala melompat keluar dengan tiba-tiba!")
                    nyawa -= 30
                    if nyawa > 0:
                        dramatic_print(f"Kamu selamat tetapi terluka parah! Kehilangan 30 nyawa. Sisa nyawa: {nyawa}")
                    else:
                        print_lose_ascii()
                        break
                        
            elif "intip" in pilihan_rumah or "jendela" in pilihan_rumah:
                # Elemen keberuntungan: 50% chance terlihat serigala
                keberuntungan = random.randint(1, 100)
                if keberuntungan <= 50:
                    nyawa -= 20
                    dramatic_print("Saat mengintip, kamu melihat serigala yang memakai pakaian nenek!")
                    if nyawa > 0:
                        dramatic_print(f"Kamu lari ketakutan dan kehilangan 20 nyawa. Sisa nyawa: {nyawa}")
                    else:
                        print_lose_ascii()
                        break
                else:
                    dramatic_print("Kamu mengintip dan melihat nenek asli sedang mempersiapkan teh.")
                    dramatic_print("Pintu terbuka sendiri dan nenek menyambutmu dengan hangat!")
                    print_win_ascii()
                    menang = True
                    break
            else:
                dramatic_print("Pilihan tidak dikenali di depan rumah. Coba lagi tanpa penalti.")
                
        elif "hutan" in pilihan or "serigala" in pilihan:
            # Elemen keberuntungan: 40% chance selamat dari hutan
            keberuntungan = random.randint(1, 100)
            nyawa -= 20
            
            if keberuntungan <= 40:
                dramatic_print("Kamu memasuki Hutan Serigala tetapi untung berhasil bersembunyi.")
                if nyawa > 0:
                    dramatic_print(f"Kamu kehilangan 20 nyawa. Sisa nyawa: {nyawa}")
                    dramatic_print("Serigala lewat tanpa melihatmu. Sekarang jalan dengan hati-hati menuju Rumah Nenek!")
                else:
                    print_lose_ascii()
                    break
            else:
                dramatic_print("Di Hutan Serigala, kamu bertemu serigala yang lapar dan agresiif!")
                if nyawa > 0:
                    dramatic_print(f"Kamu terluka dan kehilangan 20 nyawa. Sisa nyawa: {nyawa}")
                    dramatic_print("Serigala mengejar tetapi kamu berhasil escape ke tepi hutan.")
                else:
                    print_lose_ascii()
                    break
        else:
            dramatic_print("Pilihan tidak dikenali. Silakan ketik 'Rumah Nenek' atau 'Hutan Serigala'.")

    if nyawa <= 0 and not menang:
        print_lose_ascii()
    
    return menang


def main():
    while True:
        hasil = game_utama()
        dramatic_print("\n" + "="*50)
        main_lagi = input(f"Mau main lagi, {nama}? ").strip().lower()
        
        if main_lagi != "y" and main_lagi != "yes":
            dramatic_print("Terima kasih telah bermain! Sampai jumpa lagi, pemberani!")
            break


if __name__ == "__main__":
    main()
