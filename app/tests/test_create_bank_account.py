import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko,self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został odnaleziony")
    
    def test_pesel_with_len_10(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krotki pesel zostal przyjety za prawdilowy")

    def test_pesel_with_len_12(self):
        konto = Konto(self.imie, self.nazwisko, "123456789000")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za dlugi pesel zostal przyjety za prawdilowy")

    def test_empty(self):
        konto = Konto(self.imie, self.nazwisko, "")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Nie podany pesel")

    def test_wrong_prefix_promo(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.saldo,0, "Saldo nie jest zerowe!")

    def test_wrong_sufix_promo(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_123sadd")
        self.assertEqual(konto.saldo,0, "Saldo nie jest zerowe!")

    def test_wrong_len_promo(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_correct_promo(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "promocja nie zostala naliczona")

    # def test_promo_year_59 (self):
    # def test_promo_year_61 (self):
    # def test_promo_year_60 (self):
    # def test_promo_year_2001 (self):
    # def test_promo_year_2001_wrong_promo (self):
    # def test_promo_year_ (self):