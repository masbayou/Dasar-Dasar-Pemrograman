pembeli = str(input('Nama Pelanggan\t: '))
produk = str(input('Produk Pilihan\t: '))

if(produk == 'Kipas Angin'):
    harga = 1000000
    print('Harga Produk\t: %i' % (harga))

elif(produk == 'TV'):
    harga = 2000000
    print('Harga Produk\t: %i' % (harga))

elif(produk == 'Mesin Cuci'):
    harga = 3000000
    print('Harga Produk\t: %i' % (harga))
elif(produk == 'AC'):
    harga = 4000000
    print('Harga Produk\t: %i' % (harga))
else:
    harga = 5000000
    print('Harga Produk\t: %i' % (harga))

jumlah_produk = int(input("Jumlah Beli\t: "))
total_belanja = harga * jumlah_produk
print('Harga Kotor\t: %i ' % (total_belanja))

if(produk == 'Kulkas' and jumlah_produk >= 5):
    diskon = 0.20 * total_belanja
    print('Diskon\t\t: %i' % (diskon))
elif(produk == 'AC' and jumlah_produk >= 3):
    diskon = 0.10 * total_belanja
    print('Diskon\t\t: %i' % (diskon))
else:
    diskon = 0.05 * total_belanja
    print('Diskon\t\t: %i' % (diskon))

ppn = (total_belanja - diskon) * 0.10
print('PPN\t\t: %i' % (ppn))

harga_bersih = (total_belanja - diskon) + ppn 
print('Harga Bersih\t: %i ' % (harga_bersih))
