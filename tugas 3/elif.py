 # input
print('HASIL UJIAN')
nilai = int(input('Masukkan nilai : '))

# proses
if nilai > 80 :
    transkip = 'A'
elif nilai > 60 :
    transkip = 'B'
elif nilai > 40 :
    transkip = 'C'
elif nilai > 20 :
    transkip = 'D'
else :
    transkip = 'E'

# output
print('Nilai transkip :',transkip)
print('---------------')