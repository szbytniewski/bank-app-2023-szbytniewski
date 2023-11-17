import unittest

from ..KontoOsobiste import KontoOsobiste
from ..RejestrKont import RejestrKont

class TestAccountRegister(unittest.TestCase):
    personal_data = {
        "name": "Adam",
        "surname": "Nowak",
        "pesel": "66092909876"
    }

    @classmethod
    def setUpClass(cls):
        konto = KontoOsobiste(cls.personal_data["name"], cls.personal_data["surname"], cls.personal_data["pesel"])
        RejestrKont.add_account(konto)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.listaKont = []

    def test_add_account(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        RejestrKont.add_account(konto)
        self.assertEqual(RejestrKont.ammount_of_accounts(),2)

    def test_ammount_of_accounts(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        self.assertEqual(RejestrKont.ammount_of_accounts(),2)
        RejestrKont.add_account(konto)
        self.assertEqual(RejestrKont.ammount_of_accounts(),3)

    def test_search_account_by_pesel(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto2 = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        RejestrKont.add_account(konto) 
        self.assertIn(konto,RejestrKont.search_by_pesel('66092909876'))
        self.assertNotIn(konto2,RejestrKont.search_by_pesel('66092909876'))
        self.assertEqual(RejestrKont.search_by_pesel('66092909871'), False)
        