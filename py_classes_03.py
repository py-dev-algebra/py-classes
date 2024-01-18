

baza = {}
brojac = 0

class FizickaOsoba:
    def __init__(self, prezime, ime, email, mobitel, adresa) -> None:
        self.prezime = prezime
        self.ime = ime
        self.email = email
        self.mobitel = mobitel
        self.adresa = adresa


class PravnaOsoba:
    def __init__(self, ime, email, mobitel, adresa, djelatnost) -> None:
        self.ime = ime
        self.email = email
        self.mobitel = mobitel
        self.adresa = adresa
        self.djelatnost = djelatnost




def kreiraj_kupca(je_firma: bool = True):
    global brojac
    global baza

    adresa = input('Upisite postanska adresu: ')
    email = input('Upisite email: ')
    prezime = ''
    
    if je_firma:
        naziv = input('Upisite naziv: ')
    else:
        naziv = input('Upisite ime: ')
        prezime = input('Upisite prezime: ')

    baza[brojac + 1] = {
        'ime': naziv,
        'prezime': prezime,
        'adresa': adresa,
        'email': email
    }


while True:

    print('NASLOV')
    print()
    print('1. kreiraj korisnika')
    print('2. kreiraj firmu')
    print('3. izlaz')
    print()

    izbor = int(input('Izaberite jedan broj ispred akcije koju zelite pokrenuti: '))

    match izbor:
        case 1:
            kreiraj_kupca(je_firma=False)
            
        case 2:
            kreiraj_kupca()

        case 3:
            break


print('Dovidenja!')

