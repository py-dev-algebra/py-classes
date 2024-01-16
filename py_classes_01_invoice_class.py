

class Racun:
    def __init__(self, 
                 racun_broj: str, 
                 racun_datum_izdavanja: str, 
                 racun_stavke: dict):
        self.racun_broj = racun_broj
        self.racun_datum_izdavanja = racun_datum_izdavanja
        self.racun_stavke = racun_stavke
        self.racun_ukupan_iznos = 0.00
        self.racun_pdv = 0.00
        self.racun_ukupan_iznos_pdv = 0.00

        self.izrazunaj_ukupni_iznos()


    def izrazunaj_ukupni_iznos(self):
        for cijena in self.racun_stavke.values():
            self.racun_ukupan_iznos += cijena
        
        self.racun_pdv = self.racun_ukupan_iznos * 0.25
        self.racun_ukupan_iznos_pdv = self.racun_ukupan_iznos + self.racun_pdv

    def ispis(self):
        print()
        print(f'RACUN: {self.racun_broj}')
        print(f'DATUM: {self.racun_datum_izdavanja}')
        print(f'STAVKE:')
        for proizvod, cijena in self.racun_stavke.items():
            print(f'\t{proizvod}\t{cijena} EUR')
        print(f'UKUPNO: {self.racun_ukupan_iznos} EUR')
        print(f'PDV: {self.racun_pdv} EUR')
        print(f'UKUPNO s PDV: {self.racun_ukupan_iznos_pdv} EUR')
        print()












racuni = []
racun1_stavke = {
    'Laptop': 499.99,
    'Torba za laptop': 49.99,
    'Monitor': 899.99,
    'Python za pocetnike': 29.99
}
racun_1 = Racun('R-1-2024-49', '15.01.2024.', racun1_stavke)
racuni.append(racun_1)
# racun_1.ispis()

racun2_stavke = {
    'Laptop': 899.99,
    'Torba za laptop': 79.99,
    'Monitor': 699.99
}
racun_2 = Racun('R-1-2024-50', '16.01.2024.', racun2_stavke)
racuni.append(racun_2)
# racun_2.ispis()


for racun in racuni:
    racun.ispis()    
    print(racun.racun_broj)
    print()
