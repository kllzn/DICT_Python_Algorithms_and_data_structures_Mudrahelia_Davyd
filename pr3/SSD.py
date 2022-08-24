from SSD_list import Samsung, Kingston


class SSD:
    manufacture: str
    model: str
    storage: str
    formfactor: str
    interface: str
    redingspeed: str

    def __init__(self, manufacture: str, model: str, formfactor: str,
                 mod_storage_readingspeed: list, interface: str):
        self.manufacture = manufacture
        self.model = model
        self.mod, self.storage, self.readingspeed = mod_storage_readingspeed
        self.formfactor = formfactor
        self.interface = interface

    def __repr__(self) -> str:
        return f"{self.manufacture} {self.model}{self.mod} {self.storage}GB {self.formfactor} " \
               f"{self.readingspeed} MHz {self.interface}"

    def __eq__(self, other):
        return self.manufacture == other.manufacture and \
               self.model == other.model and \
               self.mod == other.mod and \
               self.storage == other.storage and \
               self.readingspeed == other.readingspeed and \
               self.interface == other.interface

    def __print_unknown(self) -> str:
        return f"""Твердотельный накопитель: {self.model}{self.mod}
Производитель: {self.manufacture}
Формфактор: {self.formfactor}
Объем памяти: {self.storage}
Интерфейс подключения {self.interface}
Отсутствует"""

    def __print_known(self, year) -> str:
        return f"""Твердотельный накопитель: {self.prefix} {self.model} {self.mod}
Производитель: {self.manufacture}
Формфактор: {self.formfactor}
Объем памяти: {self.storage}GB
Скорость считываня: {self.readingspeed} Mb/S
Год выпуска: {year}
Интерфес подключения {self.interface}
{'-' * 40}"""

    def get_info(self) -> str:
        year: int = 0
        if self.manufacture.strip().lower() == "Kingston":
            for i in Kingston:
                if self.model in i:
                    year = Kingston[i]
            self.prefix = ""
        elif self.manufacture.strip().lower() == "Samsung":
            for i in Samsung:
                if self.model in i:
                    year = Samsung[i]
            self.prefix = ""
        else:
            return self.__print_unknown()
        return self.__print_known(year)
