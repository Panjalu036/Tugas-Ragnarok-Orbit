class persegi_panjang (object): 
    def __init__(method, p, l):
        method.panjang = p
        method.lebar = l
        
    def info(method):
        print("Sebuah Persegi panjang memliki banyak rumus")

class keliling(persegi_panjang):
    def __init__(method, p, l):
        method.panjang = p
        method.lebar = l
        
    def rumus(method):
        print("Keliling persegi panjang adalah :", (2*method.panjang)+(2*method.lebar))

class luas(persegi_panjang):
    def __init__(method, p, l):
        super().__init__(p,l)
        
    def rumus(method):
        print("luas persegi panjang adalah :", method.panjang*method.lebar)
        
class volume(persegi_panjang):
    def __init__(method,p,l,t):
        method.panjang = p
        method.lebar = l
        method.tinggi = t
        
    def rumus(method):
         print("volume persegi panjang adalah :", method.panjang*method.lebar*method.tinggi)