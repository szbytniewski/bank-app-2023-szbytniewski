import unittest
from parameterized import parameterized

from ..KontoOsobiste import KontoOsobiste

class TestParameterizedLoanReq(unittest.TestCase):
    imie = "Sebastian"
    nazwisko = "Zbytniewski"
    pesel = "01282874666"

    def setUp(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([100, 100, 100], 500, True, 500),
        ([-100, 100, -100, 100, 1000], 700, True, 700),
        ([-100, 20000, -100, 100, -1000],1000, True, 1000),
        ([100], 666, False, 0),
        ([-100, 100, 100, 100, -600, 200], 500, False, 0),
    ])
    def test_taking_loan(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.history = historia
        is_credit_accepted = self.konto.taking_loan(wnioskowana_kwota)
        self.assertEqual(is_credit_accepted, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)