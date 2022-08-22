from SSD_list import kingston, samsung


class RAM:
    manufacture: str
    model: str
    interface: str
    storage: str
    formfactor: str
    readingspeed: str

    def __init__(self, manufacture: str, model: str, interface: str, storage: str, formfactor: str, readingspeed: str):
        self.manufacture = manufacture
        self.model = model
        self.interface = interface
        self.storage = storage
        self.formfactor = formfactor
        self.readingspeed = readingspeed
        self.check()

    def check(self):
        year = None
        model = "".join(str(self.model)).split()
        if self.manufacture == "Kingston":
            for i in kingston.keys():
                if model[0] in i:
                    year = kingston.get(i)
                    self.info(year)
            return year
        elif self.manufacture == "Samsung":
            for i in samsung.keys():
                if model[0] in i:
                    year = samsung.get(i)
                    self.info(year)
            return year
        else:
            print(f"""{"-"*70}
Подобная информация о твердотельном накопителе {self.model} от производителя {self.manufacture},
с форм-фактором {self.formfactor}
выпущен в {year} году с такими характеристиками: 
объёмом памяти в {self.storage},
интерфейсом подключения {self.interface}
и скоростью считывания в {self.readingspeed} 
Отсутствует.
{"-"*70}""")

    def info(self, year):
        print(f"""{"-"*70}
Тврдотельный накопитель {self.model} от производителя {self.manufacture},
с форм-фактором {self.formfactor}
выпущен в {year} году с такими характеристиками: 
объёмом памяти в {self.storage},
интерфейсом подключения {self.interface}
и скоростью считывания в {self.readingspeed}.
{"-"*70}""")


if __name__ == "__main__":
    ram1 = RAM("Kingston", "A400", "SATA III", "240GB", "2.5", "500 Mb/S")
    ram2 = RAM("Kingston", "HyperX Fury 3D", "SATA III", "480GB", "2.5", "500 Mb/S")
    ram3 = RAM("Samsung", "860 EVO series", "SATA III", "250GB", "M.2", "550 Mb/S")
    ram4 = RAM("GoodRam", "S400u", "SATA III", "240GB", "M.2", "550 Mb/S")
