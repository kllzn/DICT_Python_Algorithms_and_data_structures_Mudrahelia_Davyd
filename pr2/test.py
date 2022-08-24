from SSD import SSD
from generator import Generator


def test_ssd():
    s = SSD("Kingston", "KC600", "SATA III", ["", 256, 560.0], "2.5")
    assert s.manufacture == "Kingston"
    assert s.model == "KC600"
    assert s.interface == "2.5"
    assert s.mod == ""
    assert s.storage == 256
    assert s.readingspeed == 560.0
    assert s.formfactor == "SATA III"


def test_ssd_get_info():
    s = SSD("Kingston", "KC600", "2.5", ["", 256, 560.0], "SATA III")
    assert isinstance(s.get_info(), str)


def test_gen_single_type():
    r = Generator()
    i = r.generator()
    assert isinstance(i.manufacture, str)
    assert isinstance(i.model, str)
    assert isinstance(i.interface, str)
    assert isinstance(i.mod, str)
    assert isinstance(i.storage, int)
    assert isinstance(i.readingspeed, float)
    assert isinstance(i.formfactor, str)

def test_gen_1000_type():
    r = Generator()
    i = r.generate_1000()
    assert isinstance(i, list)
    assert len(i) == 1000


def test_gen_10000_type():
    r = Generator()
    i = r.generate_10000()
    assert isinstance(i, list)
    assert len(i) == 10000

