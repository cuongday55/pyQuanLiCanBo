class CanBo:
    def __init__(self , maCanBo="" , ten="" , tuoi=0 , gioiTinh="" , diaChi="" , luongCoBan=0.0):
        self.__maCanBo = maCanBo
        self.__ten = ten
        
        if(int(tuoi) <= 0):
            self.__tuoi = 0
        else:
            self.__tuoi = int(tuoi)
            
        if(gioiTinh != "nam" and gioiTinh != "nu" and gioiTinh != "khac"):
            self.__gioiTinh = "khac"
        else:
            self.__gioiTinh = gioiTinh
        self.__diaChi = diaChi
        if(float(luongCoBan) <= 0.0):
            self.__luongCoBan = 0.0
        else:
            self.__luongCoBan = float(luongCoBan)

    def get_maCanBo(self):
        return self.__maCanBo

    def set_maCanBo(self, maCanBo):
        self.__maCanBo = maCanBo


    def get_ten(self):
        return self.__ten

    def set_ten(self, ten):
        self.__ten = ten

    def get_tuoi(self):
        return self.__tuoi

    def set_tuoi(self, tuoi) -> int:
        if(tuoi < 0):
            self.__tuoi = 0
        else:
            self.__tuoi = int(tuoi)

    def get_gioiTinh(self):
        return self.__gioiTinh

    def set_gioiTinh(self, gioiTinh):
        if(gioiTinh != "nam" and gioiTinh != "nu" and gioiTinh != "khac"):
            self.__gioiTinh = "khac"
        else:
            self.__gioiTinh = gioiTinh

    def get_diaChi(self):
        return self.__diaChi

    def set_diaChi(self, diaChi):
        self.__diaChi = diaChi

    def get_luongCoBan(self) ->float:
        return self.__luongCoBan

    def set_luongCoBan(self, luongCoBan):
        if(luongCoBan < 0):
            self.__luongCoBan = 0.0
        else:
            self.__luongCoBan = float(luongCoBan)

    def __str__(self) -> str:
        return f"maCanBo: {self.get_maCanBo()} ten: {self.get_ten()} tuoi: {self.get_tuoi()} gioiTinh: {self.get_gioiTinh()} diaChi: {self.get_diaChi()} luongCB: {self.get_luongCoBan()}" 
        
    