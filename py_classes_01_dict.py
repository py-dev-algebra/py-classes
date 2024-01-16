bank_accounts = {
    'BA-2024-01-00001': {
        'company': {
            'name': 'Algebra d.o.o.',
            'hq_address': {
                'street': "Ilica 123",
                'postal_code': '10000',
                'city': 'Zagreb'
            },
            'oib': '12345678901',
            'manager': 'Pero Peric'
        },
        'currency': ' €',
        'transactions': [
            {
                'date': '16.01.2024.',
                'amount': 2000.00,
                'description': 'Uplata prilikom otvaranja racuna',
                'transaction_type': 'depo'
            }
        ],
        'balance': 2000.00
    },
    'BA-2024-01-00002': {
        'company': {
            'name': 'Algebra d.o.o.',
            'hq_address': {
                'street': "Ilica 123",
                'postal_code': '10000',
                'city': 'Zagreb'
            },
            'oib': '12345678901',
            'manager': 'Pero Peric'
        },
        'currency': ' CHF',
        'transactions': [
            {
                'date': '16.01.2024.',
                'amount': 20000.00,
                'description': 'Uplata prilikom otvaranja racuna',
                'transaction_type': 'depo'
            }
        ],
        'balance': 20000.00
    }
}


print(bank_accounts['BA-2024-01-00001']['company']['name'])

# bank_accounts.account_number.company.name
