from .Konto import Konto

class KontoFirmowe(Konto):
    express_transfer_fee = 5

    def __init__(self, name, nip):
        self.name = name
        self.saldo = 0
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip
