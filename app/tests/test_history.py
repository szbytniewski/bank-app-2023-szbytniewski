import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe

class TestHistory(unittest.TestCase):
    personal_data = {
        "name": "Adam",
        "surname": "Nowak",
        "pesel": "01282874666"
    }

    company_data = {
        "name": "Dziam dziam",
        "nip": "123456789"
    }

    def test_history_personal(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        konto.saldo = 50
        konto.przelew_wychodzacy(50)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.history,[-50,100],"Historia sie nie zgadza")

    def test_history_company(self):
        konto = KontoFirmowe(self.company_data["name"], self.company_data["nip"])
        konto.saldo = 100
        konto.zaksieguj_przelew_przychodzacy(15)
        konto.przelew_wychodzacy(90)
        konto.zaksieguj_przelew_przychodzacy(3)
        self.assertEqual(konto.history,[15,-90,3], "Historia sie nie zgadza")

    def test_history_personal_express(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        konto.saldo = 50
        konto.przelew_wychodzacy_exspressowy_personal(20)
        konto.zaksieguj_przelew_przychodzacy(50)
        konto.przelew_wychodzacy_exspressowy_personal(10)
        self.assertEqual(konto.history,[-20,-1,50,-10,-1],"Historia sie nie zgadza")

    def test_history_company_express(self):
        konto = KontoFirmowe(self.company_data["name"], self.company_data["nip"])
        konto.saldo = 50
        konto.przelew_wychodzacy_exspressowy_comapny(20)
        konto.zaksieguj_przelew_przychodzacy(50)
        konto.przelew_wychodzacy_exspressowy_comapny(10)
        self.assertEqual(konto.history,[-20,-5,50,-10,-5],"Historia sie nie zgadza")