
from tugas_oop_produk import Produk

print("================================")
print("   SISTEM PEMBELIAN PRODUK")
print("================================")

jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

daftar_produk = []
total_seluruh = 0

for i in range(jumlah_produk):
    print("\nProduk ke-", i + 1)
    print("--------------------------------")

    nama = input("Nama produk  : ")
    harga = int(input("Harga produk : Rp"))
    jumlah_beli = int(input("Jumlah beli  : "))

    produk = Produk(nama, harga)

    produk.tampilkan_info()

    total_produk = produk.hitung_total(jumlah_beli)

    print("Jumlah beli  :", jumlah_beli)
    print("Total produk : Rp{:,.0f}".format(total_produk))

    daftar_produk.append(produk)
    total_seluruh += total_produk

if jumlah_produk > 0:
    diskon = daftar_produk[0].hitung_diskon(total_seluruh)
else:
    diskon = 0

total_bayar = total_seluruh - diskon

print("\n================================")
print("       HASIL PEMBELIAN")
print("================================")
print("Total Pembelian : Rp{:,.0f}".format(total_seluruh))
print("Diskon 5%       : Rp{:,.0f}".format(diskon))
print("Total Bayar     : Rp{:,.0f}".format(total_bayar))
print("================================")
