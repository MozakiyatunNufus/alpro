# BUAT SET --> bracket, constructor
mySet = {'s', 'e', 't', 1}
mySet2 = set(('s', 'e', 't', 2))

# UNORDERED --> urutan tidak sama 
print('Data :', mySet)
print('Data :', mySet2)
print('--------------')

# UNDUPLICATABLE --> unique
mySet = {'s', 'e', 't', 1, 1}  # Duplikat akan diabaikan
mySet2 = set(('s', 'e', 't', 2, 2))  # Duplikat akan diabaikan
print('Duplikat :', mySet)
print('Duplikat :', mySet2)
print('--------------------')

# UNINDEXED --> tidak memiliki index
# Anda tidak dapat mengakses elemen dengan indeks
# Sebagai gantinya, kita bisa menggunakan loop untuk menampilkan elemen
print('Elemen dalam mySet:')
for element in mySet:
    print(element)
print('--------------------')

# UNCHANGEABLE --> tidak dapat dirubah
# Anda tidak dapat mengubah elemen dalam set
# Sebagai gantinya, kita bisa membuat set baru
mySet = {'s', 'e', 't', 1, 9}  # Membuat set baru dengan nilai yang diubah
print('Hasil Edit :', mySet)
print('-------------------')

# TAMBAH DATA --> add
mySet.add(5)
print('Hasil Add :', mySet)
print('------------------')

# HAPUS DATA
# pop: random, remove: spesific
mySet.pop()  # Menghapus elemen secara acak
print('Hasil Pop :', mySet)
print('-----------------')

# ex: hapus 's' dari mySet
mySet.remove('s')  # Pastikan 's' ada dalam set sebelum menghapus
print('Hasil Remove :', mySet)
print('---------------------')
