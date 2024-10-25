from kysu import KySu
from congnhan import CongNhan
from nhanvien import NhanVien
dsCanBo = []


while True:
    print("1. Them moi can bo vao ds")
    print("2. Tim kiem theo ma can bo")
    print("3. Hien thi thong tin ve cac can bo co trong ds")
    print("4. Thoat")
    chon = input("nhap lua chon: ")
    if(chon == "1"):
        tmp = input("1. ky su 2. Cong nhan 3. Nhan vien: ")
        if(tmp == "1"):
            ma = input("nhap ma can bo: ")
            ten = input("nhap ten can bo: ")
            tuoi = input("nhap tuoi can bo: ")
            gioiTinh = input("nhap gioi tinh can bo: ")
            diaChi = input("nhap dia chi can bo: ")
            luongCB = input("nhap luong can bo: ")
            nganh = input("nhap bac can bo: ")
            hasMa = True
            for cb in dsCanBo:
                if(cb.get_maCanBo() == ma):
                    hasMa = False
                    break
            if(hasMa):   
                ks = KySu(ma , ten , tuoi , gioiTinh , diaChi ,luongCB , nganh)
                dsCanBo.append(ks)
            else:
                print("ma da ton tai!")
        elif(tmp == "2"):
            ma = input("nhap ma can bo: ")
            ten = input("nhap ten can bo: ")
            tuoi = input("nhap tuoi can bo: ")
            gioiTinh = input("nhap gioi tinh can bo: ")
            diaChi = input("nhap dia chi can bo: ")
            luongCB = input("nhap luong can bo: ")
            bac = input("nhap bac can bo: ")
            hasMa = True
            for cb in dsCanBo:
                if(cb.get_maCanBo() == ma):
                    hasMa = False
                    break
                    
            if(hasMa):   
                cn = CongNhan(ma , ten , tuoi , gioiTinh , diaChi ,luongCB , bac)
                dsCanBo.append(cn)
            else:
                print("ma da ton tai!")
        elif(tmp == "3"):
            ma = input("nhap ma can bo: ")
            ten = input("nhap ten can bo: ")
            tuoi = input("nhap tuoi can bo: ")
            gioiTinh = input("nhap gioi tinh can bo: ")
            diaChi = input("nhap dia chi can bo: ")
            luongCB = input("nhap luong can bo: ")
            congViec = input("nhap congViec can bo: ")
            hasMa = True
            for cb in dsCanBo:
                if(cb.get_maCanBo() == ma):
                    hasMa = False
                    break
                    
            if(hasMa):   
                nv = NhanVien(ma , ten , tuoi , gioiTinh , diaChi ,luongCB , congViec)
                dsCanBo.append(nv)
            else:
                print("ma da ton tai!")
        else:
            print("lua chon khong ton tai!")
    elif(chon == "2"):
        ma = input("nhap ma can tim: ")
        hasCB = True
        for canBo in dsCanBo:
            if(canBo.get_maCanBo() == ma):
                hasCB = False
                print(canBo)
                break
        if(hasCB):
            print("khong tim thay!")
    elif(chon == "3"):
        for canBo in dsCanBo:
            print(canBo)
    
    elif(chon == "4"):
        break
    else:
        print("lua chon khong ton tai!")
        