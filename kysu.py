from canbo import CanBo

class KySu(CanBo):
    def __init__(self , maCanBo="" , ten="" , tuoi=0 , gioiTinh="" , diaChi="" , luongCoBan=0.0 , nganhDaoTao="") -> None:
        super().__init__(maCanBo , ten , tuoi , gioiTinh , diaChi , luongCoBan)
        self.__nganhDaoTao = nganhDaoTao
        
        
    def get_nganhDaoTao(self) ->str:
        return self.__nganhDaoTao

    def set_nganhDaoTao(self, nganhDaoTao):
        self.__nganhDaoTao = nganhDaoTao

    def luong(self) ->float:
        return super().get_luongCoBan() * 1.7
    
    def __str__(self) -> str:
        return super().__str__() + f" nganhDaoTao: {self.get_nganhDaoTao()} luong: {self.luong()} chucvu: KySu"