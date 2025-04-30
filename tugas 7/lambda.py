# FUNCTION 
def hitung(p,l):
    luas = p*l
    return luas

print('Luas tanah (function) :',hitung(20,15))

# LAMBDA
# cara 1 : use variabel
luas = lambda p,l : p*l
print('Luas tanah (lambda_1) :',luas(20,15))

# cara 2 : directly
print('Luas tanah (lambda_2) :',(lambda p,l : p*l)(20,15))