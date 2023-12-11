import requests, datetime, os

from dotenv import load_dotenv
from .Konto import Konto

load_dotenv()

nipValidateURL = os.getenv('BANK_APP_MF_URL', 'https://wl-api.mf.gov.pl/api/search/nip/')

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
            result = self.check_nip_exsistance()
            if result == False:
                raise Exception("Nip nie istnieje w gov")
            

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

    def check_nip_exsistance(self):
        result = requests.get(nipValidateURL + self.nip + '?date=' + datetime.date.today())
        print(f"Response dla nipu: {result.status_code}, {result.json()}")
        if result.status_code == 200:
            return True
        return False
    
    # Dodac funckcje wyslanie maila