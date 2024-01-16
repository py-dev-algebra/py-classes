televizijski_aparat = {
    'dijagonala': 55,
    'sirina': 124,
    'visina': 79,
    'proizvodac': 'Grundig',
    'model': 'Turbo Mega Ultra Extra XYZ 55'
}

class TelevizijskiAparat:
    dijagonala = 55
    sirina = 124
    visina = 79
    proizvodac = 'Grundig'.upper()
    model = 'Turbo Mega Ultra Extra XYZ 55'
    je_ukljucen = False

    def ukljuci(self):
        self.je_ukljucen = True




























tv_dnevni_boravak = TelevizijskiAparat()
tv_spavaca_soba = TelevizijskiAparat()

# print(televizijski_aparat['proizvodac'])
# print(tv_dnevni_boravak.proizvodac)
# print(tv_dnevni_boravak.model)

print(tv_dnevni_boravak.je_ukljucen)
# tv_dnevni_boravak.ukljuci(tv_dnevni_boravak)
tv_dnevni_boravak.ukljuci()
print(tv_dnevni_boravak.je_ukljucen)

print(tv_spavaca_soba.je_ukljucen)
# tv_spavaca_soba.ukljuci(tv_spavaca_soba)
tv_spavaca_soba.ukljuci()
print(tv_spavaca_soba.je_ukljucen)
