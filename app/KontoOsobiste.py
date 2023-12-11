import datetime
from .Konto import Konto

class KontoOsobiste(Konto):
    def __init__(self,imie,nazwisko,pesel,promo_code = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.express_transfer_fee_personal = 1
        self.history = []


        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel
        if self.is_promo_code_correct(promo_code) and self.is_customer_eligible_for_promo(promo_code):
            self.saldo += 50
        else:
            self.saldo += 0
    
    def is_promo_code_correct(self, promo_code):
        if promo_code is None:
            return False
        if promo_code.startswith("PROM_") and len(promo_code) == 8:
            return True
        return False
        
    def is_customer_eligible_for_promo(self, pesel):
        if pesel is None:
            return False
        age_max = datetime.date.today().year - 1960
        # sprawdzamy czy zwrócony wiek osoby jest wiekszy od maksymalnego wieku przyjmowanego
        if self.customer_age_calculation(self.pesel) > age_max:
            return False
        return True

    def customer_age_calculation(self,pesel):
        if pesel is None:
            return False
        curr_year_last_2_digits = int(datetime.date.today().year)
        pesel_year_2_digits = int(pesel[0:2])
        # zakładamy ze wszystkie osoby 1900-1923 nie zyja    
        if pesel_year_2_digits >= 00 and pesel_year_2_digits <= 23:
            pesel_year_2_digits += 2000
        else:
            pesel_year_2_digits += 1900

        return curr_year_last_2_digits - pesel_year_2_digits
    
    def check_n_deposits_condition(self,n):
        if(len(self.history) < n):
            return False
        for acconting in self.history[-n:]:
            if acconting < 0:
                return False
        return True
    
    def sum_of_last_n_elements_condition(self,n):
        if(len(self.history) < n):
            return False
        return sum(self.history[-n:])

    def taking_loan(self,kwota):
        if(self.check_n_deposits_condition(3) or self.sum_of_last_n_elements_condition(5) > kwota):
            self.saldo = self.saldo + kwota
            return True
        return False
    
    # Dodac funkcje wyslanie maila
    
