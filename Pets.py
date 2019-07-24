from datetime import date
from datetime import datetime

class Dono:
    def __init__(self, dono, idade):
        self.dono = dono
        self.idade = idade

class Pet(Dono):
    def __init__(self, nome, dt_nasc, idade, dono):
        super().__init__(dono, idade)
        self.nome = nome
        self.dt_nasc = dt_nasc
    
dono = input('Digite o nome do dono: ')
idade = input('Digite a idade do dono: ')
nome = input('Digite um nome do pet: ')
dt_nasc = input('Digite a data de nascimento do pet: ')
dt_hj = date.today()

nasc = datetime.strptime( dt_nasc, '%d/%m/%Y').date()
idade_pet = int(abs((dt_hj - nasc).days) / 365.33)

pet = Pet(nome, idade_pet, idade, dono)

print(f'O nome do pet é {pet.nome}, sua idade é {pet.dt_nasc} anos, seu dono é {pet.dono} e a idade de seu dono é {pet.idade} anos')