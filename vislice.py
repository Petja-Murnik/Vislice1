import bottle
import model

SKRIVNOST = 'MARIBOr'

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0,"C:\\Users\\petja\\OneDrive\\Dokumenti\\UVP\\Vislice1\\views")
@bottle.get('/')
def osnovna_stran():
    return bottle.template("index.tpl")

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', id_igre, secret=SKRIVNOST , path='/')
    bottle.redirect('/igra/')



@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    (igra,stanje) = vislice.igre[id_igre]
    return bottle.template("igra.tpl", id_igre = id_igre, igra = igra, poskus = stanje )

@bottle.post("/igra/")
def ubibaj():
    id_igre = bottle.request.get_cookie('idigre', secret = SKRIVNOST)
    crka = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def serve_pictures(picture):
    return bottle.static_file(picture, root="C:\\Users\\petja\\OneDrive\\Dokumenti\\UVP\\Vislice1\\img")

bottle.run(reloader=True, debug=True) 