# function 1
def tanah(panjang,lebar):
    luas = panjang * lebar
    return luas

# function 2
def harga(luas,hpm):
    jual = luas * hpm
    print('Harga jual tanah :',jual)
    print('------------------')

# call funtion
luas = tanah(5,3)
harga(luas,1000)