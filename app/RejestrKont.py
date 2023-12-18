from .KontoOsobiste import KontoOsobiste
from pymongo import MongoClient

class RejestrKont:
    client = MongoClient('localhost', 27017)
    db = client['bank-app']
    collection = db['konto']
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
    
    @classmethod
    def save(cls):
        cls.collection.delete_many({})
        for konto in cls.listaKont:
            cls.collection.insert_one(konto.__dict__)
        return True

    @classmethod
    def load(cls):
        cls.listaKont.clear()
        for konto_data in cls.collection.find():
            konto = KontoOsobiste(konto_data["imie"], konto_data["nazwisko"], konto_data["pesel"])
            konto.history = konto_data["history"]
            konto.saldo = konto_data["saldo"]
            cls.listaKont.append(konto)
        return True

