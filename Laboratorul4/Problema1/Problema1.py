def determina_starea_finala(secventa):
    stari = {'A', 'B'}
    tranzitii = {
        ('A', '0'): 'B',
        ('A', '1'): 'A',
        ('B', '0'): 'A',
        ('B', '1'): 'B'
    }
    
    stare_curenta = 'A'
    
    for simbol in secventa:
        if (stare_curenta, simbol) in tranzitii:
            stare_curenta = tranzitii[(stare_curenta, simbol)]
        else:
            print("Tranzitie nepermisa pentru starea curenta {} si simbolul {}".format(stare_curenta, simbol))
            return None
    return stare_curenta

secvente = ["010", "110", "1001"]
for secventa in secvente:
    print("Pentru secventa '{}', starea finala este: {}".format(secventa, determina_starea_finala(secventa)))
