from canbo import CanBo

class NhanVien(CanBo):
    def __init__(self , maCanBo="" , ten="" , tuoi=0 , gioiTinh="" , diaChi="" , luongCoBan=0.0 , congViec = "") -> None:
        super().__init__(maCanBo , ten , tuoi , gioiTinh , diaChi , luongCoBan)
        self.__congViec = congViec
        
        
    def get_congViec(self) ->str:
        return self.__congViec

    def set_congViec(self, congViec):
        self.__congViec = congViec

    def luong(self) ->float:
        return super().get_luongCoBan() * 1.7
    
    def __str__(self) -> str:
        return super().__str__() + f" congViec: {self.get_congViec()} luong: {self.luong()} chucvu: NhanVien"