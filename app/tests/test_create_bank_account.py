import unittest

from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    working_promo_code = "PROM_XYZ"

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste(self.imie, self.nazwisko,self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został odnaleziony")
    
    def test_pesel_with_len_10(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krotki pesel zostal przyjety za prawdilowy")

    def test_pesel_with_len_12(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "123456789000")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za dlugi pesel zostal przyjety za prawdilowy")

    def test_empty(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Nie podany pesel")

    def test_wrong_prefix_promo(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "prom_123")
        self.assertEqual(konto.saldo,0, "Promocja nie została zaliczona")

    def test_wrong_sufix_promo(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "PROM_123sadd")
        self.assertEqual(konto.saldo,0, "Promocja nie została zaliczona")

    def test_wrong_len_promo(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "PROM_")
        self.assertEqual(konto.saldo, 0, "Promocja nie została zaliczona")

    def test_correct_promo(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "promocja nie zostala naliczona")

    def test_promo_year_59 (self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "59111832855", self.working_promo_code)
        self.assertEqual(konto.saldo, 0 ,"Promocja nie została zaliczona")

    def test_promo_year_61 (self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "61042888766", self.working_promo_code)
        self.assertEqual(konto.saldo, 50, "Promocja została zaliczona")

    def test_promo_year_60 (self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "60081777978", self.working_promo_code)
        self.assertEqual(konto.saldo, 50, "Promocja została zaliczona")

    def test_promo_year_2001 (self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "01282874666", self.working_promo_code)
        self.assertEqual(konto.saldo, 50, "Promocja została zaliczona")

    def test_promo_year_2001_wrong_promo (self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "01282874666", "PROM")
        self.assertEqual(konto.saldo, 0, "Promocja nie została zaliczona")

    def test_promo_year_2001_correct_promo (self):
        konto = KontoOsobiste(self.imie, self.nazwisko, "01282874666", self.working_promo_code)
        self.assertEqual(konto.saldo, 50, "Promocja została zaliczona")

    def test_correct_promo_eligibility(self):
        result = KontoOsobiste.is_customer_eligible_for_promo(self,None)
        self.assertEqual(result, False, "Niepoprawny pesel!")

    def test_correct_promo_age(self):
        result = KontoOsobiste.customer_age_calculation(self,None)
        self.assertEqual(result, False, "Niepoprawny pesel!")

