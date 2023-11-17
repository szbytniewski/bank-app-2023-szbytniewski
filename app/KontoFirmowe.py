from .Konto import Konto

class KontoFirmowe(Konto):

    def __init__(self, name, nip):
        self.name = name
        self.saldo = 0
        self.express_transfer_fee_comapny = 5
        self.history = []

        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip

    def check_credit_ammount(self,n):
        if(self.saldo >= n*2):
            return True
        return False

    def check_history(self):
        for zus in self.history:
            if(zus==-1775):
                return True
        return False


    def taking_loan(self, kwota):
        if(self.check_credit_ammount(kwota) and self.check_history()):
            self.saldo = self.saldo + kwota
            return True
        return False