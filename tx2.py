from abc import ABC, abstractmethod

class Hang:
    def __init__(self, ten, sl, gia):
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.tien = sl * gia

    @staticmethod
    def nhap():
        return Hang(
            input('Nhập tên: '),
            int(input('Nhập số lượng: ')),
            float(input('Nhập đơn giá: '))
        )

class Phieu:
    def __init__(self, ma, date, ma_ncc, ten_ncc, diachi):
        self.ma = ma
        self.date = date
        self.ma_ncc = ma_ncc
        self.ten_ncc = ten_ncc
        self.diachi = diachi
        self.ds = []

    def taods(self):
        n = int(input('Nhập số lượng hàng: '))
        self.ds = [Hang.nhap() for _ in range(n)]

    @staticmethod
    def nhap():
        return Phieu(
            input('Nhập mã: '),
            input('Nhập ngày: '),
            input('Nhập mã NCC: '),
            input('Nhập tên NCC: '),
            input('Nhập địa chỉ: ')
        )
    def __str__(self):
        # 1. Phần tiêu đề phiếu
        res = '=' * 80 + '\n'
        res += f"{'PHIEU NHAP HANG':^80}\n"
        res += f"{'Ma phieu:':<15} {self.ma:<25} {'Ngay lap:':<15} {self.date}\n"
        res += f"{'Ma NCC:':<15} {self.ma_ncc:<25} {'Ten NCC:':<15} {self.ten_ncc}\n"
        res += f"{'Dia chi:':<15} {self.diachi}\n"
        res += '-' * 80 + '\n'

        # 2. Tiêu đề bảng hàng hóa
        res += f"{'Ten hang':<25} | {'So luong':>10} | {'Don gia':>15} | {'Thanh tien':>15}\n"
        res += '-' * 80 + '\n'

        # 3. Nội dung danh sách hàng
        tong_tien = 0
        for h in self.ds:
            res += f"{h.ten:<25} | {h.sl:>10} | {h.gia:>15,.0f} | {h.tien:>15,.0f}\n"
            tong_tien += h.tien

        # 4. Phần chân phiếu
        res += '-' * 80 + '\n'
        res += f"{'TONG CONG:':<55} {tong_tien:>20,.0f}\n"
        res += '=' * 80
        return res

def main():
    a = Phieu.nhap()
    a.taods()
    print(a)

if __name__ == "__main__":
    main()
