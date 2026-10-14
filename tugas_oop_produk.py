
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print("Nama Produk :", self.nama)
        print("Harga Produk: Rp{:,.0f}".format(self.harga))

    def hitung_total(self, jumlah_beli):
        return self.harga * jumlah_beli

    def hitung_diskon(self, total_pembelian):
        if total_pembelian > 5000:
            return total_pembelian * 0.05
        else:
            return 0
