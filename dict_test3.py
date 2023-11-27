contacts = {
    'John Kennedy' : {
        'birthday' : '29 may 1917', 'city' : 'Brookline',
        'phone' : '555-555-555'
    },
    'Arnold Schwarzenegger' : {
        'birthday' : '30 july 1947', 'city' : 'Gradec',
        'phone' : '777-777-777'
    },
    'Donald Trump':{
        'birthday' : '14 july 1946', 'city' : 'New York',
        'phone' : '666-666-666'
    }
}

for person in contacts:
    print(person)
    for data in contacts[person]:
        print(contacts[person][data])