class Konto:
    def __init__(self):
        self.saldo = 0

    def check_if_int(self,kwota):
        if isinstance(kwota,int):
            return True
        else:
            return False
   
    def zaksieguj_przelew_przychodzacy(self, kwota):
        if kwota > 0 and self.check_if_int(kwota):
            self.saldo += kwota
            self.history.append(kwota)
            

    def przelew_wychodzacy(self, kwota):
        if kwota > 0 and kwota <= self.saldo and self.check_if_int(kwota):
            self.saldo -= kwota
            self.history.append(kwota*(-1))
    
    def przelew_wychodzacy_exspressowy_comapny(self, kwota):
        if kwota > 0 and kwota <= self.saldo and self.check_if_int(kwota):
            self.saldo -= kwota
            self.saldo -= self.express_transfer_fee_comapny
            self.history.append(kwota*(-1))
            self.history.append(self.express_transfer_fee_comapny*(-1))


    def przelew_wychodzacy_exspressowy_personal(self, kwota):
        if kwota > 0 and kwota <= self.saldo and self.check_if_int(kwota):
            self.saldo -= kwota
            self.saldo -= self.express_transfer_fee_personal
            self.history.append(kwota*(-1))
            self.history.append(self.express_transfer_fee_personal*(-1))
    