import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreatebankAccount(unittest.TestCase):
    name = " JDG"
    nip = "1234567890"

    def test_tworzenie_konta_poprawny_nip(self):
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Name incorrect!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "Nip incorrect!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_tworzenie_konta_z_niepoprawnym_nipem(self):
        konto = KontoFirmowe(self.name, "123456789")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")
