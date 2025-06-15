class User:
    first_name = 'No name'
    last_name = 'No name'

    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name

    def sayFirstName(self):
        print(self.first_name)

    def sayLastName(self):
        print(self.last_name)

    def sayFullName(self):
        print(f'{self.first_name} {self.last_name}')
