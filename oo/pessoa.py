class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.filhos = list(filhos)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Ola'

if __name__ == "__main__":
    guilherme = Pessoa(nome='Guilherme', idade=20)
    Edson = Pessoa(guilherme, nome='Edson', idade=51)
    print(Edson.cumprimentar())
    for filho in Edson.filhos:
        print(f'Nome: {Edson.nome}, Filho: {filho.nome}')
    Edson.sobrenome = 'Silva'
    print(Edson.sobrenome)
    del Edson.sobrenome
    print(Edson.__dict__)
