# CREATE --> bracket, constructor
myTuple = ('Alif', 83)
myTuple2 = tuple(('Alif', 'Alfy'))

# ORDERED --> urutan data tetap
print('Data :', myTuple)
print('Data :', myTuple2)
print('-------------------')

# DUPLICATE --> data ganda
myTuple = ('Alif', 83, 83)
myTuple2 = tuple(('Alif', 'Alfy', 'Alfy'))
print('Duplikat :', myTuple)
print('Duplikat :', myTuple2)
print('---------------------')

# INDEX --> 0
# ex: tampilkan no. index angka 83
myIndex = myTuple.index(83)
print('Index angka 83 :', myIndex)
print('--------------')

# UNCHANGEABLE --> tidak dapat dirubah
# ex: ubah data index 1 dengan 90
# Ini akan menghasilkan error, karena tuple tidak dapat diubah
# Sebagai gantinya, kita bisa membuat tuple baru
myTuple = ('Alif', 90)  # Membuat tuple baru dengan nilai yang diubah
print('Hasil Edit :', myTuple)
print('----------------')
