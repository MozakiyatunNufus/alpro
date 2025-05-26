# BUAT LIST --> bracket, constructor
myList = [5, 7, 3]
myList2 = list(('a', 'b', 'c'))

# ORDERED --> urutan data tetap
print('Data :', myList)
print('Data :', myList2)
print('----------------')

# DUPLICATE --> data ganda
myList = [5, 7, 3, 3]
myList2 = list(('a', 'b', 'c', 'c'))
print('Duplikat :', myList)
print('Duplikat :', myList2)
print('---------------------')

# INDEX --> 0
# ex: tampilkan nomer index angka 7
myIndex = myList.index(7)
print('Index angka 7 :', myIndex)
print('-----------------')

# CHANGE
# TAMBAH DATA
# -> append: last, insert: index
myList.append(8)
print('Hasil Append :', myList)
print('----------------------')

# ex: tambahkan angka 9 pada index 1
myList.insert(1, 9)
print('Hasil Insert :', myList)
print('---------------------')

# HAPUS DATA
# -> pop: last, remove: spesific
myList.pop()
print('Hasil Pop :', myList)
print('------------------')

# ex: hapus angka 7 dari myList
myList.remove(7)  # FIXED: tambahkan parameter 7
print('Hasil Remove :', myList)
print('---------------------')

# EDIT DATA
# ex: ganti angka pada index 1 dengan 10
myList[1] = 10  # FIXED: ganti dengan nilai yang lebih jelas
print('Hasil Edit :', myList)  # FIXED: ubah label menjadi 'Edit'
print('---------------------')

