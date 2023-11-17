from .Konto import Konto

class RejestrKont:
    listaKont = []

    @classmethod
    def add_account(cls, konto):
        cls.listaKont.append(konto)

    @classmethod
    def search_by_pesel(cls,pesel):
        listOfTheSame = []
        for konto in cls.listaKont:
            if konto.pesel == pesel:
                listOfTheSame.append(konto)
        return listOfTheSame if len(listOfTheSame) != 0 else False

    @classmethod
    def ammount_of_accounts(cls):
        return len(cls.listaKont)