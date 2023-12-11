import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe

@patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance')
class TestCreatebankAccount(unittest.TestCase):
    name = "JDG"
    nip = "8461627563"

    def test_tworzenie_konta_poprawny_nip(self):
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Name incorrect!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "Nip incorrect!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")


    def test_tworzenie_konta_z_niepoprawnym_nipem(self, mock_check_nip_exsistance):
        konto = KontoFirmowe(self.name, "123456789")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "NIP incorrect")

    def test_tworzenie_konta_z_nie_istniejacym_nipem(self, mock_check_nip_exsistance):
        mock_check_nip_exsistance.return_value = False
        with self.assertRaises(Exception) as context:
            konto = KontoFirmowe(self.name, "8461627563")
        self.assertTrue("Nip nie istnieje w gov" in str(context.exception))


    # @patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance')
    def test_tworzenie_konta(self, mock_check_nip_exsistance):
        mock_check_nip_exsistance.return_value = True
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Nazwa firmy nie została zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "Nip nie został zapisany")
