from datetime import datetime

# Misalkan pertandingan dimulai pada pukul 15:00:00
waktu_mulai = datetime.strptime("15:00:00", "%H:%M:%S")

def catat_waktu_gol(waktu_mulai):
    # Waktu saat gol tercipta
    waktu_gol = datetime.now()
    
    # Menghitung waktu berlangsungnya pertandingan
    waktu_berlangsung = waktu_gol - waktu_mulai
    jam = waktu_berlangsung.seconds // 3600
    menit = (waktu_berlangsung.seconds // 60) % 60
    detik = waktu_berlangsung.seconds % 60
    
    # Menghitung menit ke berapa gol tercipta
    menit_ke = waktu_berlangsung.seconds // 60
    
    # Keterangan waktu saat gol tercipta
    waktu_gol_str = waktu_gol.strftime("%H:%M:%S")
    
    return waktu_gol_str, jam, menit, detik, menit_ke

# Contoh penggunaan
waktu_gol_str, jam, menit, detik, menit_ke = catat_waktu_gol(waktu_mulai)

print(f"Gol tercipta pada pukul {waktu_gol_str} (Menit ke-{menit_ke}), setelah pertandingan berlangsung selama {jam} jam, {menit} menit, {detik} detik.")