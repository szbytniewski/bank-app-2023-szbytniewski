from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste



app = Flask(__name__)


@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
   ilosc = RejestrKont.ammount_of_accounts()
   return jsonify({"iloscKont": ilosc}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.search_by_pesel(pesel)
    if konto != None:
        return jsonify(konto.__dict__), 200
    else:
        return jsonify({"message": "Nie ma podanego konta"}), 404

@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.search_by_pesel(dane["pesel"]) is None:
        konto = KontoOsobiste(dane["name"], dane["surname"], dane["pesel"])
        RejestrKont.add_account(konto)
        return jsonify({"message": "Konto stworzone"}), 201
    else:
        return jsonify({"message": "Konto z takim peselem jest juz stworzone"}), 409

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def aktualizuj_Dane_po_peselu(pesel):
    konto = RejestrKont.search_by_pesel(pesel)
    if konto is not None:
        updated = request.json
        
        for key, value in updated.items():
            setattr(konto, key, value)
        
        return jsonify(konto.__dict__), 200
    else:
        return jsonify({"message": "Nie ma podanego konta"}), 404

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def usun_konto_po_peselu(pesel):
    konto = RejestrKont.search_by_pesel(pesel)
    if konto is not None:
        RejestrKont.listaKont.remove(konto)
        return jsonify({"message": "Konto zostało usunięte"}), 200
    else:
        return jsonify({"message": "Nie ma podanego konta"}), 404

@app.route("/api/accounts/<pesel>/transfer", methods=["POST"])
def przelew_po_peselu(pesel):
    konto = RejestrKont.search_by_pesel(pesel)
    if konto is not None:
        dane = request.get_json()
        if dane["type"] == "incoming":
            konto.zaksieguj_przelew_przychodzacy(dane["ammount"])
        elif dane["type"] == "outgoing":
            konto.przelew_wychodzacy(dane["ammount"])
        return jsonify({"message": "Zlecenie przyjeto do realizacji"}), 200
    else:
        return jsonify({"messeage": "Nie ma podanego konta"}), 404