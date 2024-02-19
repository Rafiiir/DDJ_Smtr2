belanja = [
    {"produk":"Baju", "jumlah":20},
    {"produk":"Celana", "jumlah":15},
    {"produk":"Sepatu", "jumlah":25},
    {"produk":"Tas", "jumlah":10},
    ]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["jumlah"]

print("Total Belanja : ", total_belanjaan)