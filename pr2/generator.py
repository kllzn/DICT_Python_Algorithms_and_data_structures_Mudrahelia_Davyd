import random
from SSD import SSD
from SSD_list import Kingston, Samsung, K_interface, S_interface


class Generator:
    def _create_manufacture(self) -> str:
        self.manufacture = random.choice(["Kingston", "Samsung"])
        return self.manufacture

    def _create_series(self) -> str:
        if self.manufacture == "Kingston":
            self.series = random.choice(list(Kingston.keys()))
        else:
            self.series = random.choice(list(Samsung.keys()))
        return self.series

    def _create_type(self) -> str:
        if self.manufacture == "Kingston":
            self.interface = K_interface[self.series]
            if len(self.interface) > 1:
                self.interface = self.interface[random.randint(0, 1)].split()
            elif len(self.interface) == 1:
                self.interface.append("".join(self.interface))
        else:
            self.interface = S_interface[self.series]
        return str("".join(self.interface))

    def _memory_and_modification(self) -> list:
        if self.manufacture == "Kingston":
            if self.series == "A400":
                self.memory = random.choice([120, 240, 480, 960])
                self.readingspeed = 500.0
                self.mod = ""
                self.formfactor = "2.5"
            if self.series == "HyperX Fury 3D":
                self.memory = random.choice([120, 240, 480])
                self.frequency = 500.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "DC450R":
                self.memory = random.choice([480, 960, 1920, 3840, 7680])
                self.frequency = 560.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "KC600":
                self.memory = random.choice([256, 512, 1024, 2048])
                self.frequency = 550.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "KC3000":
                self.memory = random.choice([512, 1024, 2048, 4096])
                self.frequency = 7000.0
                self.mod = ""
                self.formfactor = "M.2"
            elif self.series == "HyperX Fury Renegade":
                self.memory = random.choice([500, 1000, 2000, 4000])
                self.frequency = 7300.0
                self.mod = ""
                self.formfactor = "M.2"
            else:
                self.mod, self.memory, self.frequency = "ERROR", 0, 0.0
        else:
            if self.series == "870 QVO":
                self.memory = random.choice([1024, 2048, 4096, 8192])
                self.frequency = 560.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "860 QVO":
                self.memory = random.choice([1024, 2048, 4096])
                self.frequency = 550.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "860 EVO Series":
                self.memory = random.choice([256, 512, 1024, 2048, 4096])
                self.frequency = 550.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "870 EVO Series":
                self.memory = random.choice([256, 512, 1024, 2048, 4096])
                self.frequency = 560.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "860 PRO series":
                self.memory = random.choice([256, 512, 1024, 2048, 4096])
                self.frequency = 561.0
                self.mod = ""
                self.formfactor = "2.5"
            elif self.series == "970 EVO plus":
                self.memory = random.choice([256, 512, 1024])
                self.frequency = 3500.0
                self.mod = ""
                self.formfactor = "M.2"
            elif self.series == "980":
                self.memory = random.choice([256, 512, 1024])
                self.frequency = 3500.0
                self.mod = ""
                self.formfactor = "M.2"
            else:
                self.mod, self.memory, self.frequency = "ERROR", 0, 0.0
        return [self.mod, self.memory, self.frequency]

    def generator(self) -> SSD:
        return SSD(self._create_manufacture(), self._create_series(), self._create_type(),
                   self._memory_and_modification(), self.formfactor)

    def generate_1000(self) -> list:
        return [self.generator() for i in range(1000)]

    def generate_10000(self) -> list:
        return [self.generator() for i in range(10000)]


if __name__ == "__main__":
    gen = Generator()
    [print(i) for i in gen.generate_10000()]
