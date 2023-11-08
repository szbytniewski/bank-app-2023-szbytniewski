import unittest

from ..KontoOsobiste import KontoOsobiste

class TestLoanRequirements(unittest.TestCase):
    personal_data = {
        "name": "Adam",
        "surname": "Nowak",
        "pesel": "01282874666"
    }
    
    def test_loan_3_deposits(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        konto.saldo = 5
        konto.zaksieguj_przelew_przychodzacy(10)
        konto.zaksieguj_przelew_przychodzacy(20)
        konto.zaksieguj_przelew_przychodzacy(5)
        if_granted = konto.taking_loan(1000)
        self.assertTrue(if_granted)
        self.assertEqual(konto.saldo,1040)

    def test_loan_5_transaction(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        konto.history = [-100,200,-50,100,100]
        if_granted = konto.taking_loan(200)
        self.assertTrue(if_granted)
        self.assertEqual(konto.saldo,200)

    def test_loan_5_transaction_wrong(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        konto.history = [-100,-200,-50,100,100]
        if_granted = konto.taking_loan(200)
        self.assertFalse(if_granted)
        self.assertEqual(konto.saldo,0)

    def test_loan_not_enough(self):
        konto = KontoOsobiste(self.personal_data["name"], self.personal_data["surname"],self.personal_data["pesel"])
        konto.history = [-100,-200]
        if_granted = konto.taking_loan(200)
        self.assertFalse(if_granted)
        self.assertEqual(konto.saldo,0)