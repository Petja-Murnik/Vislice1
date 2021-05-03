import random   

stevilo_dovoljenih_napak = 9
pravilna_crka = '+'
ponovljena_crka = 'o'
napacna_crka = '-'
zmaga = 'W'
poraz = 'X'
ZACETEK = 'S'


class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo] 

    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        return vse_crke and stevilo_dovoljenih_napak >= self.stevilo_napak() 

    def poraz(self):
        return stevilo_dovoljenih_napak < self.stevilo_napak()

    def pravilni_del_gesla(self):
        delni = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in self.crke:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni.strip()

    def nepravilni_ugibi(self): 
        return ' '.join(self.napacne_crke())
    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return ponovljena_crka
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return zmaga
            else:
                return pravilna_crka
        else:
            self.crke.append(crka)
            if self.poraz():
                return poraz
            else:
                return napacna_crka

with open('Vislice1/besede.txt', 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper()for beseda in f.readlines()]

 

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])

class Vislice:

    def __init__(self):
        self.igre = {}
    
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        (igra,_) = self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)
        



#testno_geslo = 'DEŽUJE'
#testne_crke = ['A','E','O','D','J','K','Ž']
#igra = Igra(testno_geslo, testne_crke)
#print(testno_geslo)
        