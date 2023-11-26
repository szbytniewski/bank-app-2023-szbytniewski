from .Konto import Konto

class RejestrKont:
    listaKont = []

    @classmethod
    def add_account(cls, konto):
        cls.listaKont.append(konto)

    @classmethod
    def search_by_pesel(self, pesel):
        for konto in self.listaKont:
            if konto.pesel == pesel:
                return konto
        return None
    @classmethod
    def ammount_of_accounts(cls):
        return len(cls.listaKont)
    