import unittest
from unittest.mock import patch

from ..KontoFirmowe import KontoFirmowe


class TestCreatebankAccount(unittest.TestCase):
    name = "JDG"
    nip = "8461627563"

    @patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance')
    def test_tworzenie_konta_poprawny_nip(self, mock_check_nip_exsistance):
        mock_check_nip_exsistance.return_value = True
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Name incorrect!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "Nip incorrect!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    @patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance')
    def test_tworzenie_konta_z_niepoprawnym_nipem(self, check_nip_exsistance):
        konto = KontoFirmowe(self.name, "123456789")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "NIP incorrect")

    @patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance')
    def test_tworzenie_konta_z_nie_istniejacym_nipem(self, check_nip_exsistance):
        with patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance') as mock_check_nip_exsistance:
            mock_check_nip_exsistance.return_value = False
            with self.assertRaises(Exception) as context:
                konto = KontoFirmowe(self.name, "8461627563")
        self.assertTrue("Nip nie istnieje w gov" in str(context.exception))

    @patch('app.KontoFirmowe.KontoFirmowe.check_nip_exsistance')
    def test_tworzenie_konta(self, mock_check_nip_exsistance):
        mock_check_nip_exsistance.return_value = True
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Nazwa firmy nie została zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "Nip nie zostalo zapisany")

    @patch('app.KontoFirmowe.requests.get')
    def test_sprawdzanie_istnienia_nip_prawidlowy(self, mock_get):
        mock_get.return_value.status_code = 200
        konto = KontoFirmowe(self.name, self.nip)
        wynik = konto.check_nip_exsistance()
        self.assertTrue(wynik, "Oczekiwano True dla istniejącego NIP")

    @patch('app.KontoFirmowe.requests.get')
    def test_sprawdzanie_istnienia_nip_nieprawidlowy(self, mock_get):
        mock_get.return_value.status_code = 404
        konto = KontoFirmowe(self.name, "123456789")
        wynik = konto.check_nip_exsistance()
        self.assertFalse(wynik, "Oczekiwano False dla nieistniejącego NIP")