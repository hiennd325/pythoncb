class Hang:
    def __init__(self):
        ten = input('ten hang: ')
        dongia = (dg:=(float(input('nhap don gia: '))))
        soluong = (sl:=(float(input('nhap so luong: '))))
        thanhtien = dg*sl

class Phieu:
    def __init__(self,ma,ngay,ncc,tenncc,diachi):
        self.ma = input('nhap ma: ')
        self.ngay = input('nhap ngay: ')
        self.ncc = input('nhap ncc: ')
        self.tenncc = input('nhap ten nha cung cap: ')
        self.diachi = input('nhap dia chi: ')
        self.hangs = []

    def taophieu(self):
        n = int(input('nhap so luong hang: '))
        self.hangs = [Hang() for _ in n]
        
    def __str__(self):
        res = '+','='*15,'+'
        res += 