# input
print('HASIL UJIAN')
nilai = int(input('Masukkan nilai : '))

# proses
if nilai >= 70 :
    status = 'Lulus'
    if nilai >= 80 :
        predikat = 'Memuaskan'
    else :
        predikat = 'Cukup'
else :
    status = 'Tidak Lulus'
    predikat = 'Kurang'

# output
print('Status :',status)
print('Predikat :',predikat)
print('-------------------')