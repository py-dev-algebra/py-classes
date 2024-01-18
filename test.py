baza = {}
brojac = 0


class Osoba:
    def __init__(self, ime, email_adresa, mobitel, adresa) -> None:
        self.ime = ime
        self.email_adresa = email_adresa
        self.mobitel = mobitel
        self.adresa = adresa


class FizickaOsoba(Osoba):
    def __init__(self, prezime, ime, email, mobitel, adresa) -> None:
        super().__init__(ime, email, mobitel, adresa)
        self.prezime = prezime


class PravnaOsoba(Osoba):
    def __init__(self, ime, email, mobitel, adresa, djelatnost) -> None:
        super().__init__(ime, email, mobitel, adresa)
        self.djelatnost = djelatnost




def kreiraj_kupca(je_firma: bool = True):
    global brojac
    global baza

    adresa = input('Upisite postanska adresu: ')
    e_mail = input('Upisite email: ')
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
        'email': e_mail
    }

    kupac = FizickaOsoba(prezime=prezime, ime=naziv, mobitel='09 1234 567', adresa=adresa, email=e_mail)
    kupac.ime
    kupac.email_adresa

    kupac2 = PravnaOsoba(naziv, e_mail, '09 1234 987', adresa, 'Python programiranje')
    kupac2.djelatnost
    kupac2.email_adresa

    baza[brojac + 1] = kupac
    baza[brojac + 1] = kupac2


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