class Person:
  def __init__(self, nama,jenis_kelamin,umur):
    self.nama = nama
    self.jenis_kelamin = jenis_kelamin
    self.umur = umur

  def printname(self):
    print(self.nama)
    print(self.jenis_kelamin)
    print(self.umur)

class Karyawan(Person):
    def __init__(self,gaji):
        self.__gaji = gaji
    def set_gaji(self, gaji):
        if 0 <= gaji <= 100:
            self.__gaji = gaji
        else:
            print("gaji must be between 0 and 100")
    def get_gaji(self):
        return self.__gaji 

        
class Rekening:
    def __init__(self, No_Rekening,PIN):
        self.No_Rekening = No_Rekening
        self.__PIN = 0

    def set_PIN(self, PIN):
        if 0 <= PIN <= 100:
            self.__PIN = PIN
        else:
            print("PIN must be between 0 and 100")

    def get_PIN(self):
        return self.__PIN 

x = Person("Syikbi", "Laki-laki",30)
x.printname()
