
import model


ponovni_zagon = 'p'
izhod = 'i'


def izpis_igre(igra):
    tekst = f'''#############################\n
    Pravilni del gesla :{igra.pravilni_del_gesla()} \n
    Število poskusov : {model.stevilo_dovoljenih_napak - igra.stevilo_napak()}\n 
    Nepravilne črke: {igra.nepravilni_ugibi()}
#######################\n'''
    return tekst


def izpis_zmage(igra):
    tekst = f'''#############################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo:{igra.pravilni_del_gesla()}\n 
#################\n'''
    return tekst

def izpis_poraza(igra):
    tekst = f'''##########################\n 
    Porabili ste vse poskuse.\n
    Pravilno geslo je bilo: {igra.geslo}\n
###############################\n'''
    return tekst

def zahtevaj_vnos():
    return input('Vnesite črko:')

def zahtevaj_moznost():
    return input('vnesite možnost:')


def ponudi_moznosti():
    tekst = f''' Vpišite črko za izbor naslednjih možnosti:\n
    {ponovni_zagon}: ponovni zagon igre\n
    {izhod}: izhod\n
    '''
    return tekst

def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == ponovni_zagon:
        igra = model.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return izhod

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.zmaga:
            print(izpis_zmage(igra))
            igra = izberi_ponovitev()
            if igra == izhod:
                break
        elif odziv == model.poraz:
            print(izpis_poraza(igra))
            igra = izberi_ponovitev()
            if igra == izhod:
                break
        else:
            print(izpis_igre(igra))
         

pozeni_vmesnik()