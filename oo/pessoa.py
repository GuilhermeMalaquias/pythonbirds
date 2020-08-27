class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Teste'

if __name__ == "__main__":
    pessoa = Pessoa()
    print(pessoa.cumprimentar())
    print(pessoa.nome)
    pessoa.nome = 'Guilherme'
    print(f'Nome:{pessoa.nome} Idade: {pessoa.idade}')
