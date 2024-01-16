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
                 program: int = 0,
                 glasnoca: int = 10,
                 je_ukljucen: bool = False) -> None:
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.program = program
        self.glasnoca = glasnoca
        self.je_ukljucen = je_ukljucen

    def ukljuci(self):
        self.je_ukljucen = True

    def iskljuci(self):
        self.je_ukljucen = False

    def reguliraj_glasnocu(self, razina_glasnoce):
        if razina_glasnoce <= 50 and razina_glasnoce >= 0:
            self.glasnoca = razina_glasnoce

    def utisaj(self):
        self.glasnoca -= 1

    def pojacaj(self):
        self.glasnoca += 1

    def mute(self):
        self.glasnoca = 0

    def promijeni_program(self, novi_program):
        self.program = novi_program





























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

#region STARO
# print(televizijski_aparat['proizvodac'])
# print(tv_dnevni_boravak.proizvodac)
# print(tv_dnevni_boravak.model)

# print(tv_dnevni_boravak.je_ukljucen)
# # tv_dnevni_boravak.ukljuci(tv_dnevni_boravak)
# tv_dnevni_boravak.ukljuci()
# print(tv_dnevni_boravak.je_ukljucen)

# print(tv_spavaca_soba.je_ukljucen)
# # tv_spavaca_soba.ukljuci()
# # print(tv_spavaca_soba.je_ukljucen)
# # tv_spavaca_soba.iskljuci()
# # print(tv_spavaca_soba.je_ukljucen)

# print(tv_dnevni_boravak.model)
# print(tv_spavaca_soba.model)
# # tv_spavaca_soba.model = 'Novi model'
# print(tv_spavaca_soba.model)

#endregion

print(tv_dnevni_boravak.glasnoca)
tv_dnevni_boravak.pojacaj()
tv_dnevni_boravak.utisaj()
tv_dnevni_boravak.reguliraj_glasnocu(45)
print(tv_dnevni_boravak.glasnoca)
tv_dnevni_boravak.mute()
print(tv_dnevni_boravak.glasnoca)
tv_dnevni_boravak.pojacaj()
print(tv_dnevni_boravak.glasnoca)

novi_program = int(input('Upisite novi program'))
tv_dnevni_boravak.promijeni_program(novi_program)

# tv_dnevni_boravak.model = 'Novi naziv modela' -. OVAKO NE
# tv_dnevni_boravak.change_model('Novi naziv modela') # Ovako DA
