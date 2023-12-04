import requests
import unittest

from ..RejestrKont import RejestrKont

class TestAccountCrud(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000/api/accounts"

    def test_1_create_account(self):
        response = requests.post(self.url, json={"name": "Jan", "surname": "Kowalski", "pesel": "12345678901"})
        self.assertEqual(response.status_code, 201)

    def test_2_get_account_by_pesel(self):
        response = requests.get(self.url + "/12345678901")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"express_transfer_fee_personal": 1,
        "history": [], "imie": "Jan", "nazwisko": "Kowalski", "pesel": "12345678901", "saldo": 0})

    def test_3_check_for_404(self):
        response = requests.get(self.url + "/12345678977")
        self.assertEqual(response.status_code, 404)

    def test_4_patch(self):
        response = requests.patch(self.url + "/12345678901", json={"imie": "Adam"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"express_transfer_fee_personal": 1,
        "history": [], "imie": "Adam", "nazwisko": "Kowalski", "pesel": "12345678901", "saldo": 0})

    def test_5_check_for_patch_404(self):
        response = requests.patch(self.url + "/12345678977")
        self.assertEqual(response.status_code, 404)

    def test_6_check_if_deleted(self):
        response = requests.delete(self.url + "/12345678901")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Konto zostało usunięte"})

    def test_7_check_if_unique_pesel(self):
        response = requests.post(self.url, json={"name": "Jan", "surname": "Kowalski", "pesel": "22345678901"})
        response2 = requests.post(self.url, json={"name": "Jan", "surname": "Kowalski", "pesel": "22345678901"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response2.status_code, 409)

    def test_8_transfer_by_pesel_search(self):
        requests.post(self.url, json={"name": "Jan", "surname": "Kowalski", "pesel": "12345678901"})
        #1. Test incoming transfer
        response = requests.post(self.url + "/12345678901/transfer", json={"ammount": 500, "type": "incoming"})
        response1 = requests.get(self.url + "/12345678901")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.json()["saldo"], 500)
        #2. Test udany outgoing transfer
        response2 = requests.post(self.url + "/12345678901/transfer", json={"ammount": 100, "type": "outgoing"})
        response3 = requests.get(self.url + "/12345678901")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.json()["saldo"], 400)
        # 3. Test na nieudany outgoing transfer(not enough balance)
        response4 = requests.post(self.url + "/12345678901/transfer", json={"ammount": 500, "type": "outgoing"})
        response5 = requests.get(self.url + "/12345678901")
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.json()["saldo"], 400)
        # 4. test na nieudany incoming transfer(nie znaleziono konto)
        response6 = requests.post(self.url + "/43215678901/transfer", json={"ammount": 100, "type": "incoming"})
        self.assertEqual(response6.status_code, 404)
        

    def tearDown(self):
        requests.delete("http://127.0.0.1:5000/api/accounts" + "/22345678901")
