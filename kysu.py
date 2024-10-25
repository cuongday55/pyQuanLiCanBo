from canbo import CanBo

class KySu(CanBo):
    def __init__(self , maCanBo="" , ten="" , tuoi=0 , gioiTinh="" , diaChi="" , luongCoBan=0.0 , bac=1) -> None:
        super().__init__(maCanBo , ten , tuoi , gioiTinh , diaChi , luongCoBan)
        if(int(bac) <= 0 or int(bac) > 10):
            self.__bac = 1
        else:
            self.__bac = int(bac)
        
        
    def get_bac(self) ->int:
        return self.__bac

    def set_bac(self, bac):
        if(bac <= 0 or bac > 10):
            self.__bac = 1
        else:
            self.__bac = bac

    def luong(self) ->float:
        return super().get_luongCoBan() * 1.7
    
    def __str__(self) -> str:
        return super().__str__() + f" bac: {self.get_bac()} luong: {self.luong()} chucvu: KySu"