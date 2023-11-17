import unittest
from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe

class TestParameterizedLoanReq(unittest.TestCase):
    imie = " Dziam dziam"
    nip = "123456789"

    def setUp(self):
        self.konto = KontoFirmowe(self.imie, self.nip)

    @parameterized.expand([
        ([-1775,200,100,-50],1000, 400, True, 1400),
        ([2000,140,-200,50],2000,400,False,2000),
        ([-1775,150,2000,1000,-10000],500,500,False,500),
        ([100,100,200,-1000,200],100,1000,False,100),
        ])

    def test_taking_loan(self, historia, saldo, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.history = historia
        self.konto.saldo = saldo
        is_credit_accepted = self.konto.taking_loan(wnioskowana_kwota)
        self.assertEqual(is_credit_accepted, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)