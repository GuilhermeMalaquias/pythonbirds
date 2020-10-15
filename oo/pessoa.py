class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.filhos = list(filhos)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_statico():
        return 'Medoto estatico'

    @classmethod
    def nome_e_atributo_da_classe(cls):
        return f'{cls} {cls.olhos}'


if __name__ == "__main__":
    guilherme = Pessoa(nome='Guilherme', idade=20)
    Teste = Pessoa(nome='Teste', idade=20)
    Edson = Pessoa(guilherme, nome='Edson', idade=51)
    for filhos in Edson.filhos:
        print(filhos.nome)
    guilherme.sobrenome = "Malaquias"
    print(guilherme.sobrenome)
    guilherme.olhos = 1
    print(guilherme.olhos)
    print(Edson.olhos)
    Pessoa.olhos = 3
    del guilherme.olhos
    print(Pessoa.olhos, guilherme.olhos, Edson.olhos)
    print(Pessoa.metodo_statico(), guilherme.metodo_statico())
    print(Pessoa.nome_e_atributo_da_classe())
