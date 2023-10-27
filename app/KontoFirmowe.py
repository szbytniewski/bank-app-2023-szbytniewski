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
