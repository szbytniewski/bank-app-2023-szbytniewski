import requests
import unittest

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