import re

def citeste_fisier():
    cale_fisier = input("Introduceti calea catre fisierul text: ")
    try:
        with open(cale_fisier, 'r') as fisier:
            continut = fisier.read()
            return continut
    except FileNotFoundError:
        print("Fisierul nu a fost gasit.")
        return None

def verificare_format(continut):
    if continut is None:
        return
    
    # Definirea expresiilor regulate pentru fiecare secțiune a facturii
    exp_client = r"Client: (.+)"
    exp_produse = r"Produse: (.+)"
    exp_pret = r"Pret: (\d+(\.\d{1,2})?)"
    exp_tva = r"TVA: (\d+(\.\d{1,2})?)%"
    exp_cantitate = r"Cantitate: (\d+)"

    # Verificarea formatului utilizând expresii regulate
    erori = []
    if not re.search(exp_client, continut):
        erori.append("Eroare: Lipsesc informațiile despre client.")
    if not re.search(exp_produse, continut):
        erori.append("Eroare: Lipsesc detalii despre produse.")
    if not re.search(exp_pret, continut):
        erori.append("Eroare: Pretul nu este specificat corect.")
    if not re.search(exp_tva, continut):
        erori.append("Eroare: TVA-ul nu este specificat corect.")
    if not re.search(exp_cantitate, continut):
        erori.append("Eroare: Cantitatea nu este specificată corect.")

    return erori

def afiseaza_erori(erori):
    if erori:
        print("Au fost identificate urmatoarele erori:")
        for eroare in erori:
            print(eroare)
    else:
        print("Fisierul respecta formatul specificat.")

# Citirea fișierului text
continut = citeste_fisier()

# Verificarea formatului și identificarea erorilor
if continut:
    erori = verificare_format(continut)
    afiseaza_erori(erori)
