

racun_broj = 'R-1-2024-50'
racun_datum_izdavanja = '16.01.2024.'
racun_stavke = {
    'Laptop': 499.99,
    'Torba za laptop': 49.99,
    'Monitor': 899.99,
    'Python za pocetnike': 29.99
}
racun_ukupan_iznos = 0.00
for cijena in racun_stavke.values():
    racun_ukupan_iznos += cijena
racun_pdv = racun_ukupan_iznos * 0.25
racun_ukupan_iznos_pdv = racun_ukupan_iznos + racun_pdv

print()
print(f'RACUN: {racun_broj}')
print(f'DATUM: {racun_datum_izdavanja}')
print(f'STAVKE:')
for proizvod, cijena in racun_stavke.items():
    print(f'{proizvod}\t{cijena} EUR')
print(f'DATUM: {racun_ukupan_iznos}')
print(f'DATUM: {racun_pdv}')
print(f'DATUM: {racun_ukupan_iznos_pdv}')

# Problem s dodavanjem novog racuna