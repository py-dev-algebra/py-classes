televizijski_aparat = {
    'dijagonala': 55,
    'sirina': 124,
    'visina': 79,
    'proizvodac': 'Grundig',
    'model': 'Turbo Mega Ultra Extra XYZ 55'
}

class TelevizijskiAparat:
    def __init__(self, 
                 dijagonala: int, 
                 sirina: int, 
                 visina: int, 
                 proizvodac: str, 
                 model: str, 
                 je_ukljucen: bool = False) -> None:
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.je_ukljucen = je_ukljucen

    def ukljuci(self):
        self.je_ukljucen = True

    def iskljuci(self):
        self.je_ukljucen = False






























tv_dnevni_boravak = TelevizijskiAparat(proizvodac='Grundig',
                                       model='Model 55',
                                       dijagonala=55,
                                       sirina=125,
                                       visina=79)
tv_spavaca_soba = TelevizijskiAparat(proizvodac='Sony',
                                     model='Model 120',
                                     dijagonala=20,
                                     sirina=125,
                                     visina=79,
                                     je_ukljucen=True)

# print(televizijski_aparat['proizvodac'])
# print(tv_dnevni_boravak.proizvodac)
# print(tv_dnevni_boravak.model)

# print(tv_dnevni_boravak.je_ukljucen)
# # tv_dnevni_boravak.ukljuci(tv_dnevni_boravak)
# tv_dnevni_boravak.ukljuci()
# print(tv_dnevni_boravak.je_ukljucen)

print(tv_spavaca_soba.je_ukljucen)
# tv_spavaca_soba.ukljuci()
# print(tv_spavaca_soba.je_ukljucen)
# tv_spavaca_soba.iskljuci()
# print(tv_spavaca_soba.je_ukljucen)

print(tv_dnevni_boravak.model)
print(tv_spavaca_soba.model)
# tv_spavaca_soba.model = 'Novi model'
print(tv_spavaca_soba.model)