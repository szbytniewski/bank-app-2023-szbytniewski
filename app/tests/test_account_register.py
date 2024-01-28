import unittest
from unittest.mock import patch

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
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], "12345678901")
        konto2 = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        RejestrKont.add_account(konto) 
        self.assertEqual(RejestrKont.search_by_pesel('12345678901'), konto)
        self.assertEqual(RejestrKont.search_by_pesel('66092909871'), None)
    
    @patch('app.RejestrKont.RejestrKont.collection')
    def test_save_load_accounts(self, mock_collection):
        mock_data = [
            {"imie": "Jan", "nazwisko": "Kowalski", "pesel": "89092909875", "saldo": 1000, "history": []}
        ]
        mock_collection.find.return_value = mock_data

        RejestrKont.save()

        RejestrKont.listaKont.clear()

        RejestrKont.load()

        self.assertEqual(len(RejestrKont.listaKont), 1)
        loaded_account = RejestrKont.listaKont[0].__dict__
        self.assertEqual(loaded_account["imie"], 'Jan')
        self.assertEqual(loaded_account["nazwisko"], 'Kowalski')
        self.assertEqual(loaded_account["pesel"], '89092909875')
        self.assertEqual(loaded_account["saldo"], 1000)
        self.assertEqual(loaded_account["history"], [])